/** \class STAMuonAnalyzer
 *  Analyzer of the StandAlone muon tracks
 *
 *  $Date: 2009/10/31 05:19:45 $
 *  $Revision: 1.7 $
 *  \author R. Bellan - INFN Torino <riccardo.bellan@cern.ch>
 */

#include "RecoMuon/StandAloneMuonProducer/test/STAMuonAnalyzer.h"

// Collaborating Class Header
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/ESHandle.h"

#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"
#include "Geometry/Records/interface/GlobalTrackingGeometryRecord.h"
#include "Geometry/CommonDetUnit/interface/GlobalTrackingGeometry.h"
#include "Geometry/CommonDetUnit/interface/GeomDet.h"

#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "DataFormats/TrajectorySeed/interface/TrajectorySeedCollection.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "RecoMuon/TrackingTools/interface/MuonPatternRecoDumper.h"

#include "SimDataFormats/Track/interface/SimTrackContainer.h"

#include <DataFormats/GEMRecHit/interface/GEMRecHit.h>
#include "DataFormats/GEMRecHit/interface/GEMRecHitCollection.h"
#include "DataFormats/CSCRecHit/interface/CSCRecHit2D.h"
#include "DataFormats/CSCRecHit/interface/CSCRecHit2DCollection.h"
#include "SimDataFormats/TrackingHit/interface/PSimHitContainer.h"
 
#include "Geometry/GEMGeometry/interface/GEMGeometry.h"
#include <Geometry/GEMGeometry/interface/GEMEtaPartition.h>
#include <Geometry/Records/interface/MuonGeometryRecord.h>

#include <Geometry/CommonDetUnit/interface/GeomDet.h>
#include "DataFormats/Provenance/interface/Timestamp.h"

#include <DataFormats/MuonDetId/interface/GEMDetId.h>

#include "RecoMuon/DetLayers/interface/MuonDetLayerGeometry.h"
#include "RecoMuon/Records/interface/MuonRecoGeometryRecord.h"

#include "RecoMuon/DetLayers/interface/MuRodBarrelLayer.h"
#include "RecoMuon/DetLayers/interface/MuDetRod.h"
#include "RecoMuon/DetLayers/interface/MuRingForwardDoubleLayer.h"
#include "RecoMuon/DetLayers/interface/MuDetRing.h"
#include "SimDataFormats/TrackingAnalysis/interface/TrackingParticle.h"
#include "DataFormats/MuonDetId/interface/MuonSubdetId.h"

#include "DataFormats/TrackingRecHit/interface/TrackingRecHitFwd.h"

#include "MagneticField/Engine/interface/MagneticField.h"
#include "MagneticField/Records/interface/IdealMagneticFieldRecord.h"

#include <DataFormats/MuonDetId/interface/DTWireId.h>
#include <DataFormats/MuonDetId/interface/CSCDetId.h>
#include <DataFormats/MuonDetId/interface/GEMDetId.h>

#include "Geometry/Records/interface/GlobalTrackingGeometryRecord.h"
#include "Geometry/CommonDetUnit/interface/GlobalTrackingGeometry.h"

#include "DataFormats/Math/interface/deltaR.h"

#include "TFile.h"
#include "TH1F.h"
#include "TH2F.h"

using namespace std;
using namespace edm;

/// Constructor
STAMuonAnalyzer::STAMuonAnalyzer(const ParameterSet& pset){
  staTrackLabel_ = pset.getUntrackedParameter<edm::InputTag>("StandAloneTrackCollectionLabel");
  theSeedCollectionLabel = pset.getUntrackedParameter<string>("MuonSeedCollectionLabel");

  theRootFileName = pset.getUntrackedParameter<string>("rootFileName");

  theDataType = pset.getUntrackedParameter<string>("DataType");
  
  if(theDataType != "RealData" && theDataType != "SimData")
    cout<<"Error in Data Type!!"<<endl;

  noGEMCase_ = pset.getUntrackedParameter<bool>("NoGEMCase");

  numberOfSimTracks=0;
  numberOfRecTracks=0;
}

/// Destructor
STAMuonAnalyzer::~STAMuonAnalyzer(){
}

void STAMuonAnalyzer::beginJob(){
  // Create the root file
  theFile = new TFile(theRootFileName.c_str(), "RECREATE");
  theFile->cd();

  hPtRec = new TH1F("pTRec","p_{T}^{rec}",200,0,1000);
  hPtSim = new TH1F("pTSim","p_{T}^{gen} ",200,0,1000);

  hPTDiff = new TH1F("pTDiff","p_{T}^{rec} - p_{T}^{gen} ",400,-1000,1000);
  hPTDiff2 = new TH1F("pTDiff2","p_{T}^{rec} - p_{T}^{gen} ",400,-1000,1000);

  hPTDiffvsEta = new TH2F("PTDiffvsEta","p_{T}^{rec} - p_{T}^{gen} VS #eta",100,-2.5,2.5,200,-1000,1000);
  hPTDiffvsPhi = new TH2F("PTDiffvsPhi","p_{T}^{rec} - p_{T}^{gen} VS #phi",100,-6,6,200,-1000,1000);

  hPres = new TH1F("pTRes","pT Resolution",100,-2,2);
  h1_Pres = new TH1F("invPTRes","1/pT Resolution",100,-2,2);

  hSimEta = new TH1F("PSimEta","SimTrack #eta",100,-2.5,2.5);
  hRecEta = new TH1F("PRecEta","RecTrack #eta",100,-2.5,2.5);
  hDeltaEta = new TH1F("PDeltaEta","#Delta#eta",100,-2.5,2.5);
  hDeltaPhi = new TH1F("PDeltaPhi","#Delta#phi",100,-6,6);

  hSimPhi = new TH1F("PSimPhi","SimTrack #phi",100,-6,6);
  hRecPhi = new TH1F("PRecPhi","RecTrack #phi",100,-6,6);

  hNumSimTracks = new TH1F("NumSimTracks","NumSimTracks",100,0,100);
  hNumMuonSimTracks = new TH1F("NumMuonSimTracks","NumMuonSimTracks",10,0,10);
  hNumRecTracks = new TH1F("NumRecTracks","NumRecTracks",10,0,10);

  //Double_t nbins[] = {0,10,30,50,100,150,200,300,500,750,1000};

  hPtResVsPt = new TH2F("PtResVsPt","p_{T} Resolution vs. p_{T}",10,0,1000,50,0,2);
  hInvPtResVsPt = new TH2F("InvPtResVsPt","1/p_{T} Resolution vs. p_{T}",10,0,1000,50,0,2);
  hDPhiVsPt = new TH2F("DPhiVsPt","#Delta#phi vs. p_{T}",10,0,1000,100,-6,6);

  hDenPt = new TH1F("DenPt","DenPt",10,0,1000);
  hDenEta = new TH1F("DenEta","DenEta",100,-2.5,2.5);
  hNumPt = new TH1F("NumPt","NumPt",10,0,1000);
  hNumEta = new TH1F("NumEta","NumEta",100,-2.5,2.5);

  hPullGEM = new TH1F("PullGEM", "(x_{mc} - x_{rec}) / #sigma",500,-15.,15.);
  hPullCSC = new TH1F("PullCSC", "(x_{mc} - x_{rec}) / #sigma",500,-15.,15.);

  hGEMRecHitEta = new TH1F("GEMRecHitEta","GEM RecHits #eta",100,-2.5,2.5);

  hDR = new TH1F("DR","#Delta R (SIM-RECO)",124,-0.1,6.1);

  //hPTDiffvsEta = new TH2F("PTDiffvsEta","p_{T}^{rec} - p_{T}^{gen} VS #eta",100,-2.5,2.5,200,-1000,1000);

}

void STAMuonAnalyzer::endJob(){
  if(theDataType == "SimData"){
    cout << endl << endl << "Number of Sim tracks: " << numberOfSimTracks << endl;
  }

  cout << "Number of Reco tracks: " << numberOfRecTracks << endl << endl;
    
  // Write the histos to file
  theFile->cd();
  hPtRec->Write();
  hPtSim->Write();
  hPres->Write();
  h1_Pres->Write();
  hPTDiff->Write();
  hPTDiff2->Write();
  hPTDiffvsEta->Write();
  hPTDiffvsPhi->Write();
  hSimEta->Write();
  hRecEta->Write();
  hDeltaEta->Write();
  hDeltaPhi->Write();
  hSimPhi->Write();
  hRecPhi->Write();
  hNumSimTracks->Write();
  hNumMuonSimTracks->Write();
  hNumRecTracks->Write();
  hPtResVsPt->Write();
  hInvPtResVsPt->Write();
  hDPhiVsPt->Write();
  hDenPt->Write();
  hDenEta->Write();
  hNumPt->Write();
  hNumEta->Write();
  hPullGEM->Write();
  hPullCSC->Write();
  hGEMRecHitEta->Write();
  hDR->Write();
  theFile->Close();
}
 

void STAMuonAnalyzer::analyze(const Event & event, const EventSetup& eventSetup){
  
  cout << "Run: " << event.id().run() << " Event: " << event.id().event() << endl;
  MuonPatternRecoDumper debug;
  
  // Get the RecTrack collection from the event
  Handle<reco::TrackCollection> staTracks;
  event.getByLabel(staTrackLabel_, staTracks);

  ESHandle<MagneticField> theMGField;
  eventSetup.get<IdealMagneticFieldRecord>().get(theMGField);

  edm::ESHandle<MagneticField> magfield;
  eventSetup.get<IdealMagneticFieldRecord>().get(magfield);

  edm::ESHandle<GEMGeometry> gemGeom;
  eventSetup.get<MuonGeometryRecord>().get(gemGeom);

  edm::ESHandle<MuonDetLayerGeometry> geo;
  eventSetup.get<MuonRecoGeometryRecord>().get(geo);

  ESHandle<GlobalTrackingGeometry> theTrackingGeometry;
  eventSetup.get<GlobalTrackingGeometryRecord>().get(theTrackingGeometry);

  edm::Handle<GEMRecHitCollection> gemRecHits; 
  event.getByLabel("gemRecHits","",gemRecHits);

  edm::Handle<CSCRecHit2DCollection> cscRecHits; 
  event.getByLabel("csc2DRecHits","",cscRecHits);

  edm::Handle<edm::PSimHitContainer> GEMHits;
  event.getByLabel(edm::InputTag("g4SimHits","MuonGEMHits"), GEMHits);

  edm::Handle<edm::PSimHitContainer> CSCHits;
  event.getByLabel(edm::InputTag("g4SimHits","MuonCSCHits"), CSCHits);

  double recPt = 0.;
  double simPt = 0.;
  double simEta = 0.;
  double simPhi = 0.;

  hNumRecTracks->Fill(staTracks->size());

  int simCount = 0;
  //int numRecoTrack = 0;

  // Get the SimTrack collection from the event
  if(theDataType == "SimData"){

    	Handle<SimTrackContainer> simTracks;
    	event.getByLabel("g4SimHits",simTracks);

	//numRecoTrack = simTracks->size();
  	hNumSimTracks->Fill(simTracks->size());
    
    	numberOfRecTracks += staTracks->size();

    	SimTrackContainer::const_iterator simTrack;

    	cout<<"Simulated tracks: "<<endl;
    	for (simTrack = simTracks->begin(); simTrack != simTracks->end(); ++simTrack){

	      	if (abs((*simTrack).type()) == 13) {

			cout<<"Sim pT: "<<(*simTrack).momentum().pt()<<endl;
			simPt=(*simTrack).momentum().pt();
			cout<<"Sim Eta: "<<(*simTrack).momentum().eta()<<endl;
			simEta = (*simTrack).momentum().eta();

			cout<<"Sim Phi: "<<(*simTrack).momentum().phi()<<endl;
			simPhi = (*simTrack).momentum().phi();

			numberOfSimTracks++;
			simCount++;
			hSimEta->Fill((*simTrack).momentum().eta());
			hSimPhi->Fill((*simTrack).momentum().phi());

	      	}    

    	}

	hNumMuonSimTracks->Fill(simCount);
    	cout << endl;

  }
  
  reco::TrackCollection::const_iterator staTrack;
  
  cout<<"Reconstructed tracks: " << staTracks->size() << endl;

  Handle<SimTrackContainer> simTracks;
  event.getByLabel("g4SimHits",simTracks);

  SimTrackContainer::const_iterator simTrack;

  for (simTrack = simTracks->begin(); simTrack != simTracks->end(); ++simTrack){

	      	if (abs((*simTrack).type()) != 13) continue;

	  	for (staTrack = staTracks->begin(); staTrack != staTracks->end(); ++staTrack){//Inizio del loop sulle STA track

		    	reco::TransientTrack track(*staTrack,&*theMGField,theTrackingGeometry); 
		    	TrajectoryStateOnSurface innerTSOS = track.innermostMeasurementState();
		    
		    	//cout << debug.dumpFTS(track.impactPointTSCP().theState());

  			GlobalVector tsosVect = innerTSOS.globalMomentum();
  			math::XYZVectorD reco(tsosVect.x(), tsosVect.y(), tsosVect.z());

			double recEta = reco.eta();
			double recPhi = reco.phi();
			//cout<<"RecEta "<<recEta<<" recPhi "<<recPhi<<std::endl;
			simEta = (*simTrack).momentum().eta();
			simPhi = (*simTrack).momentum().phi();
			//cout<<"SimEta "<<simEta<<" SimPhi "<<simPhi<<std::endl;
			double dR = sqrt(pow((simEta-recEta),2) + pow((simPhi-recPhi),2));
			//cout<<"dR "<<dR<<std::endl;

			if(dR > 2) continue;
		    
		    	recPt = track.impactPointTSCP().momentum().perp();    
		    	//cout<<" p: "<<track.impactPointTSCP().momentum().mag()<< " pT: "<<recPt<<endl;
		    	//cout<<" chi2: "<<track.chi2()<<endl;
		    
		    	hPtRec->Fill(recPt);

		    	//cout << "Inner TSOS:"<<endl;
		    	//cout << debug.dumpTSOS(innerTSOS);
		    	//cout<<" p: "<<innerTSOS.globalMomentum().mag()<< " pT: "<<innerTSOS.globalMomentum().perp()<<endl;

		    	/*trackingRecHit_iterator rhbegin = staTrack->recHitsBegin();
		    	trackingRecHit_iterator rhend = staTrack->recHitsEnd();
		    
		    	cout<<"RecHits:"<<endl;
		    	for(trackingRecHit_iterator recHit = rhbegin; recHit != rhend; ++recHit){
		      		const GeomDet* geomDet = theTrackingGeometry->idToDet((*recHit)->geographicalId());
		      		//std::cout<<"detID "<<((*recHit)->geographicalId())<<" "<<geomDet<<std::endl;
		      		double r = geomDet->surface().position().perp();
		      		double z = geomDet->toGlobal((*recHit)->localPosition()).z();
		      		//cout<<"r: "<< r <<" z: "<<z <<endl;
		    	}*/
	    
		    	if(recPt && theDataType == "SimData" && abs(recEta) > 1.6 && abs(recEta) < 2.4){

		      		hDenPt->Fill(recPt);
		      		hDenEta->Fill(recEta);

		    	 	bool hasGemRecHits = false;
		      		for(trackingRecHit_iterator recHit = staTrack->recHitsBegin(); recHit != staTrack->recHitsEnd(); ++recHit){

		      			const GeomDet* geomDet = theTrackingGeometry->idToDet((*recHit)->geographicalId());
		      			//double r = geomDet->surface().position().perp();
		      			double z = geomDet->toGlobal((*recHit)->localPosition()).z();
		      			double x_reco = (*recHit)->localPosition().x();
		      			double err_x_reco = (*recHit)->localPosition().x();;
		      			double x = geomDet->toGlobal((*recHit)->localPosition()).x();
		      			double y = geomDet->toGlobal((*recHit)->localPosition()).y();
					GlobalPoint pointRecHit = GlobalPoint(x,y,z);
		      			//std::cout<<"x: "<<x<<" y: "<<y<<" r: "<< r <<" z: "<<z<<std::endl;

					if ((*recHit)->geographicalId().det() == DetId::Muon){

					if ((*recHit)->geographicalId().subdetId() == MuonSubdetId::GEM){

						//std::cout<<"GEM id: "<<GEMDetId((*recHit)->geographicalId().rawId())<<std::endl;
						hasGemRecHits = true;
						hGEMRecHitEta->Fill(pointRecHit.eta());
						std::cout<<"Eta GEMRecHits "<<pointRecHit.eta()<<std::endl;
						std::cout<<"Phi GEMRecHits "<<pointRecHit.phi()<<std::endl;

		  				for (edm::PSimHitContainer::const_iterator itHit = GEMHits->begin(); itHit != GEMHits->end(); ++itHit){
						 
						    	if (std::abs(itHit->particleType())==13){

								float x_sim = itHit->localPosition().x();
								//float err_x_sim = itHit->localPositionError().xx();
								//float y_sim = itHit->localPosition().y();
								float dX = x_sim - x_reco;
								float pull = dX/std::sqrt(err_x_reco);
								hPullGEM->Fill(pull);

						     	}

						}

					}

					else if((*recHit)->geographicalId().subdetId() == MuonSubdetId::CSC){

						//std::cout<<"CSC id: "<<CSCDetId((*recHit)->geographicalId().rawId())<<std::endl;

		  				for (edm::PSimHitContainer::const_iterator itHit = CSCHits->begin(); itHit != CSCHits->end(); ++itHit){
						 
						    	if (std::abs(itHit->particleType())==13){

								float x_sim = itHit->localPosition().x();
								//float err_x_sim = itHit->localPositionError().xx();
								//float y_sim = itHit->localPosition().y();
								float dX = x_sim - x_reco;
								float pull = dX/std::sqrt(err_x_reco);
								hPullCSC->Fill(pull);

						     	}

						}

					}

					}

		      		}

		      		if(noGEMCase_) hasGemRecHits = true;

		      		if(hasGemRecHits){

					cout<<"RecEta "<<recEta<<" recPhi "<<recPhi<<std::endl;
					cout<<"SimEta "<<simEta<<" SimPhi "<<simPhi<<std::endl;
					cout<<"dR "<<dR<<std::endl;

					hDR->Fill(dR);

		      			hPres->Fill((recPt-simPt)/simPt);
		      			hPtResVsPt->Fill(simPt, abs((recPt-simPt)/simPt));
		      			hPtSim->Fill(simPt);

		      			hPTDiff->Fill(recPt-simPt);
		      			hRecEta->Fill(recEta);

		      			hDeltaEta->Fill(simEta - recEta);
		      			hDeltaPhi->Fill(simPhi - recPhi);

		      			hRecPhi->Fill(recPhi);
		      			//hPTDiff2->Fill(track.innermostMeasurementState().globalMomentum().perp()-simPt);
		      			hPTDiffvsEta->Fill(recEta,recPt-simPt);
		      			hPTDiffvsPhi->Fill(recPhi,recPt-simPt);

		      			//if( ((recPt-simPt)/simPt) <= -0.4)
					//	cout<<"Out of Res: "<<(recPt-simPt)/simPt<<endl;

		      			h1_Pres->Fill((1/recPt - 1/simPt)/(1/simPt));
		      			hInvPtResVsPt->Fill(simPt, abs((1/recPt - 1/simPt)/(1/simPt)));

		      			hDPhiVsPt->Fill(simPt, recPhi-simPhi);

		      			hNumPt->Fill(recPt);
		      			hNumEta->Fill(recEta);

		      		}

		    	}
    
  	}//Fine loop sulle STA track

  }//Fine loop sulle SimTrack


  cout<<"---"<<endl;  
}

DEFINE_FWK_MODULE(STAMuonAnalyzer);
