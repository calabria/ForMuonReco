// -*- C++ -*-
//
// Package:    GEMRecHitsReader
// Class:      GEMRecHitsReader
// 
/**\class GEMRecHitsReader GEMRecHitsReader.cc GEMRecHitsReader/GEMRecHitsReader/src/GEMRecHitsReader.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  
//         Created:  Wed Jul 10 11:46:45 CEST 2013
// $Id$
//
//


// system include files
#include <memory>
#include <fstream>
#include <sys/time.h>
#include <string>
#include <sstream>
#include <iostream>
#include <iomanip>


// root include files
#include "TFile.h"
#include "TH1F.h"
#include "TH2F.h"
#include "TF1.h"
#include "THStack.h"
#include "TLegend.h"
#include "TLatex.h"
#include "TTree.h"
#include "TCanvas.h"
#include "TDirectoryFile.h"
#include "TGraph.h"
#include "TGraphErrors.h"
#include "TGraphAsymmErrors.h"


// user include files

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include <FWCore/Framework/interface/EventSetup.h>
#include <FWCore/Framework/interface/ESHandle.h>
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

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

#include "TrackingTools/TransientTrack/interface/TransientTrack.h"
#include "DataFormats/TrajectorySeed/interface/TrajectorySeedCollection.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "RecoMuon/TrackingTools/interface/MuonPatternRecoDumper.h"

#include "SimDataFormats/Track/interface/SimTrackContainer.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "DataFormats/Math/interface/deltaR.h"

//
// class declaration
//

class GEMRecHitsReader : public edm::EDAnalyzer {
   public:
      explicit GEMRecHitsReader(const edm::ParameterSet&);
      ~GEMRecHitsReader();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);


   private:
      virtual void beginJob() ;
      virtual void analyze(const edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;

      //virtual void beginRun(edm::Run const&, edm::EventSetup const&);
      //virtual void endRun(edm::Run const&, edm::EventSetup const&);
      //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);
      //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&);

      // ----------member data ---------------------------

      std::map<std::string,TH1F*> histContainer_;
      std::map<std::string,TH2F*> histContainer2D_; 

      edm::InputTag simHitLabel_;
      edm::InputTag recHitLabel_;
      edm::InputTag simTrackLabel_;
      edm::InputTag staTrackLabel_;

      int numGemRecHits = 0;
      int numCscRecHits = 0;
      int numGemRecHitsFromSTA = 0;
      int numCscRecHitsFromSTA = 0;

};

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
GEMRecHitsReader::GEMRecHitsReader(const edm::ParameterSet& iConfig):
  histContainer_(),
  histContainer2D_(),
  simHitLabel_(iConfig.getUntrackedParameter<edm::InputTag>("simHit")),
  recHitLabel_(iConfig.getUntrackedParameter<edm::InputTag>("recHit")),
  simTrackLabel_(iConfig.getUntrackedParameter<edm::InputTag>("simTrack")),
  staTrackLabel_(iConfig.getUntrackedParameter<edm::InputTag>("staTrack"))
{
   //now do what ever initialization is needed

}


GEMRecHitsReader::~GEMRecHitsReader()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called for each event  ------------
void
GEMRecHitsReader::analyze(const edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  using namespace edm;

  edm::ESHandle<GEMGeometry> gemGeom;
  iSetup.get<MuonGeometryRecord>().get(gemGeom);

  edm::ESHandle<MuonDetLayerGeometry> geo;
  iSetup.get<MuonRecoGeometryRecord>().get(geo);

  edm::Handle<GEMRecHitCollection> gemRecHits; 
  iEvent.getByLabel("gemRecHits","",gemRecHits);

  edm::Handle<CSCRecHit2DCollection> cscRecHits; 
  iEvent.getByLabel("csc2DRecHits","",cscRecHits);

  Handle<reco::TrackCollection> staTracks;
  iEvent.getByLabel(staTrackLabel_, staTracks);

  //std::cout<<"input "<<staTrackLabel_<<std::endl;

  ESHandle<MagneticField> theMGField;
  iSetup.get<IdealMagneticFieldRecord>().get(theMGField);

  ESHandle<GlobalTrackingGeometry> theTrackingGeometry;
  iSetup.get<GlobalTrackingGeometryRecord>().get(theTrackingGeometry);

  Handle<SimTrackContainer> simTracks;
  iEvent.getByLabel("g4SimHits",simTracks);

  edm::Handle<edm::PSimHitContainer> GEMHits;
  iEvent.getByLabel(edm::InputTag("g4SimHits","MuonGEMHits"), GEMHits);

  edm::Handle<edm::PSimHitContainer> CSCHits;
  iEvent.getByLabel(edm::InputTag("g4SimHits","MuonCSCHits"), CSCHits);

  for (GEMRecHitCollection::const_iterator recHit = gemRecHits->begin(); recHit != gemRecHits->end(); recHit++) {

	if (recHit->geographicalId().det() == DetId::Muon){

		if (recHit->geographicalId().subdetId() == MuonSubdetId::GEM){

			//std::cout<<"id: "<<GEMDetId(recHit->geographicalId().rawId())<<std::endl;
			numGemRecHits++;

		}

	}

  }

  for (CSCRecHit2DCollection::const_iterator recHit = cscRecHits->begin(); recHit != cscRecHits->end(); recHit++) {

	if (recHit->geographicalId().det() == DetId::Muon){

		if (recHit->geographicalId().subdetId() == MuonSubdetId::CSC){

			//std::cout<<"id: "<<CSCDetId(recHit->geographicalId().rawId())<<std::endl;
			numCscRecHits++;

		}

	}

  }


  //std::cout<<"Num. GEMRechHits: "<<numGemRecHits<<" Num. CSCRecHits: "<<numCscRecHits<<std::endl; 


  SimTrackContainer::const_iterator simTrack;
  reco::TrackCollection::const_iterator staTrack;
  GEMRecHitCollection::const_iterator recHit;

  int numSimHitsPerEvt = 0;
  int numRecHitsPerEvt = 0;
  int numRecHitsPerEvtStaTrack = 0;
  int numRecHitsOverlap = 0;
  int numRecHitsNoOverlap = 0;
  std::vector<GEMRecHit> matchedRecHits;
  std::vector<GlobalPoint> matchedRecHitsGP;
  std::vector<LocalPoint> matchedRecHitsLP;
  std::vector<int> matchedRecHitsStrip;

  for (edm::PSimHitContainer::const_iterator itHit = GEMHits->begin(); itHit != GEMHits->end(); ++itHit){

	if(itHit->particleType() != 13) continue;

	DetId id = DetId(itHit->detUnitId());
	GEMDetId idGem = GEMDetId(itHit->detUnitId());

	int region_sim = idGem.region();
	int layer_sim = idGem.layer();
        int chamber_sim = idGem.chamber();
        //int roll_sim = idGem.roll();

	histContainer_["hSimHitChamber"]->Fill(chamber_sim);

	GlobalPoint pointSimHit = theTrackingGeometry->idToDetUnit(id)->toGlobal(itHit->localPosition());

	//float x_sim = itHit->localPosition().x();
	float simX = pointSimHit.x();
	float simY = pointSimHit.y();
	float simPhi = pointSimHit.phi();
	float simEta = pointSimHit.eta();
	//int stripNum_sim = itHit->firstClusterStrip();

	histContainer2D_["hSimHitOcc"]->Fill(simX, simY);

	numSimHitsPerEvt++;

  	for (recHit = gemRecHits->begin(); recHit != gemRecHits->end(); recHit++) {

		GEMDetId rollId = (GEMDetId)(*recHit).gemId();
		LocalPoint recHitPos=recHit->localPosition();
		const GEMEtaPartition* rollasociated = gemGeom->etaPartition(rollId);
		const BoundPlane & GEMSurface = rollasociated->surface(); 
		GlobalPoint GEMGlobalPoint = GEMSurface.toGlobal(recHitPos);

		int region = rollId.region();
		int layer = rollId.layer();
		int chamber = rollId.chamber();
      		//int roll = rollId.roll();

		double x = GEMGlobalPoint.x();
		double y = GEMGlobalPoint.y();
		//double z = GEMGlobalPoint.z();

		double recPhi = GEMGlobalPoint.phi();
		double recEta = GEMGlobalPoint.eta();
		double dR = deltaR(simEta, simPhi, recEta, recPhi);

		histContainer_["hDR"]->Fill(dR);

		if(!(region_sim == region && layer_sim == layer)) continue;
		if(dR > 0.1) continue;

	 	histContainer_["hRecHitChamber"]->Fill(chamber);
		histContainer2D_["hRecHitOcc"]->Fill(x, y);
		numRecHitsPerEvt++;

		int stripNum = recHit->firstClusterStrip();
		//double x_reco = recHitPos.x();
		//float phi_02pi = recPhi < 0 ? recPhi + TMath::Pi() : recPhi;
		//float phiDeg = phi_02pi * 180/ TMath::Pi();

		//if(phiDeg > 5 && phiDeg < 15){

			//std::cout<<"Local x: "<<x_reco<<std::endl;
			//std::cout<<"Global x: "<<x<<" y: "<<y<<" z: "<<z<<std::endl;
			//std::cout<<"StripNumber: "<<stripNum<<std::endl;
			matchedRecHits.push_back(*recHit);
			matchedRecHitsGP.push_back(GEMGlobalPoint);
			matchedRecHitsLP.push_back(recHitPos);
			matchedRecHitsStrip.push_back(stripNum);

		//}


    	}

   	for (staTrack = staTracks->begin(); staTrack != staTracks->end(); ++staTrack){//Inizio del loop sulle STA track

		for(trackingRecHit_iterator recHit = staTrack->recHitsBegin(); recHit != staTrack->recHitsEnd(); ++recHit){

			if (!((*recHit)->geographicalId().det() == DetId::Muon)) continue;
			if (!((*recHit)->geographicalId().subdetId() == MuonSubdetId::GEM)) continue;

			GEMDetId id((*recHit)->geographicalId());
			const GeomDet* geomDet = theTrackingGeometry->idToDet((*recHit)->geographicalId());

			int region = id.region();
			int layer = id.layer();
			int chamber = id.chamber();
	      		//int roll = id.roll();

			double x = geomDet->toGlobal((*recHit)->localPosition()).x();
			double y = geomDet->toGlobal((*recHit)->localPosition()).y();
			double z = geomDet->toGlobal((*recHit)->localPosition()).z();
			GlobalPoint GEMGlobalPoint = GlobalPoint(x,y,z);

			double recPhi = GEMGlobalPoint.phi();
			double recEta = GEMGlobalPoint.eta();
			double dR = deltaR(simEta, simPhi, recEta, recPhi);

			histContainer_["hDRStaTrack"]->Fill(dR);

			if(!(region_sim == region && layer_sim == layer)) continue;
			if(dR > 0.1) continue;

		 	histContainer_["hRecHitChamberStaTrack"]->Fill(chamber);
			histContainer2D_["hRecHitOccStaTrack"]->Fill(x, y);
			numRecHitsPerEvtStaTrack++;

			//int stripNum = recHit->firstClusterStrip();
			//double x_reco = (*recHit)->localPosition().x();
			//float phi_02pi = recPhi < 0 ? recPhi + TMath::Pi() : recPhi;
			//float phiDeg = phi_02pi * 180/ TMath::Pi();

			//if(phiDeg > 5 && phiDeg < 15){

				//std::cout<<"Local x: "<<x_reco<<std::endl;
				//std::cout<<"Global x: "<<x<<" y: "<<y<<" z: "<<z<<std::endl;
				//std::cout<<"StripNumber: "<<stripNum<<std::endl;

				for(int i = 0; i < (int)matchedRecHitsGP.size(); i++){

					GlobalPoint gpTemp = matchedRecHitsGP[i];

					double xTemp = gpTemp.x();
					double yTemp = gpTemp.y();
					double zTemp = gpTemp.z();

					if((x-xTemp) == 0 && (y-yTemp) == 0 && (z-zTemp) == 0) numRecHitsOverlap++;
					else{

						numRecHitsNoOverlap++;
						histContainer2D_["hMissingRecHitsLocPos"]->Fill(matchedRecHitsLP[i].x(), matchedRecHitsStrip[i]);

					}

				}

			//}

		}

	}


  }

  histContainer_["hSimHitMult"]->Fill(numSimHitsPerEvt);
  histContainer_["hRecHitMult"]->Fill(numRecHitsPerEvt);
  histContainer_["hRecHitMultStaTrack"]->Fill(numRecHitsPerEvtStaTrack);
  histContainer_["hRecHitMultOverlap"]->Fill(numRecHitsOverlap);
  histContainer_["hRecHitMultNoOverlap"]->Fill(numRecHitsNoOverlap);

  //std::cout<<"Num. GEMRechHitsSTA: "<<numGemRecHitsFromSTA<<" Num. CSCRecHitsSTA: "<<numCscRecHitsFromSTA<<std::endl; 

}


// ------------ method called once each job just before starting event loop  ------------
void 
GEMRecHitsReader::beginJob()
{

  edm::Service<TFileService> fs;
  histContainer_["hSimHitChamber"] = fs->make<TH1F>("SimHitChamber", "SimHitChamber", 36, 0, 36);
  histContainer_["hRecHitChamber"] = fs->make<TH1F>("RecHitChamber", "RecHitChamber", 36, 0, 36);
  histContainer_["hRecHitChamberStaTrack"] = fs->make<TH1F>("RecHitChamberStaTrack", "RecHitChamberStaTrack", 36, 0, 36);

  histContainer_["hSimHitMult"] = fs->make<TH1F>("SimHitMult", "SimHitMult", 5, 0, 5);
  histContainer_["hRecHitMult"] = fs->make<TH1F>("RecHitMult", "RecHitMult", 5, 0, 5);
  histContainer_["hRecHitMultStaTrack"] = fs->make<TH1F>("RecHitMultStaTrack", "RecHitMultStaTrack", 5, 0, 5);
  histContainer_["hRecHitMultOverlap"] = fs->make<TH1F>("RecHitMultOverlap", "RecHitMultOverlap", 5, 0, 5);
  histContainer_["hRecHitMultNoOverlap"] = fs->make<TH1F>("RecHitMultNoOverlap", "RecHitMultNoOverlap", 5, 0, 5);

  histContainer_["hDR"] = fs->make<TH1F>("DR", "DR", 300, 0, 1);
  histContainer_["hDRStaTrack"] = fs->make<TH1F>("DRStaTrack", "DRStaTrack", 300, 0, 1);

  histContainer2D_["hSimHitOcc"] = fs->make<TH2F>("SimHitOcc", "SimHitOcc", 100, -260, 260, 100, -260, 260);
  histContainer2D_["hRecHitOcc"] = fs->make<TH2F>("RecHitOcc", "RecHitOcc", 100, -260, 260, 100, -260, 260);
  histContainer2D_["hRecHitOccStaTrack"] = fs->make<TH2F>("RecHitOccStaTrack", "RecHitOccStaTrack", 100, -260, 260, 100, -260, 260);

  histContainer2D_["hMissingRecHitsLocPos"] = fs->make<TH2F>("RecHitOccStaTrackLocPos", "RecHitOccStaTrackLocPos", 100, -50, 50, 400, 0, 400);

}

// ------------ method called once each job just after ending the event loop  ------------
void 
GEMRecHitsReader::endJob() 
{
}

// ------------ method called when starting to processes a run  ------------
/*
void 
GEMRecHitsReader::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a run  ------------
/*
void 
GEMRecHitsReader::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
GEMRecHitsReader::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
GEMRecHitsReader::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
GEMRecHitsReader::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(GEMRecHitsReader);
