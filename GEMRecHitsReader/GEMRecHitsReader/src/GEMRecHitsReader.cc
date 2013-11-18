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
// Original Author:  Cesare Calabria
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
#include "DataFormats/GEMDigi/interface/GEMDigiCollection.h"
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
      edm::InputTag label;

      int numGemRecHits = 0;
      int numCscRecHits = 0;

};

int countCluster(std::vector<int> firedStrips){

 	int count = 0;

	if(firedStrips.size() == 1) count++;
	else if(firedStrips.size() > 1){

		for(int i=0; i<(int)firedStrips.size(); i++){

			if(i != 0 && (firedStrips[i] - firedStrips[i-1]) == 1) count++;

		}

	}
	
	return count;

}

bool isMatched(int strip_sim, int strip, int cls){

	bool result = false;

	for(int i=0; i<cls; i++){

		if( (strip + i) == strip_sim) result = true;

	}

	return result;

}

/*bool isSimMatched(SimTrackContainer::const_iterator simTrack, edm::PSimHitContainer::const_iterator itHit)
{

  bool result = false;

  int trackId = simTrack->trackId();
  int trackId_sim = itHit->trackId();
  if(trackId == trackId_sim) result = true;

  //std::cout<<"ID: "<<trackId<<" "<<trackId_sim<<" "<<result<<std::endl;

  return result;

}*/

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
  simTrackLabel_(iConfig.getUntrackedParameter<edm::InputTag>("simTrack"))
{
   //now do what ever initialization is needed
  label = iConfig.getUntrackedParameter<std::string>("label", "simMuonGEMDigis");
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

  edm::Handle<GEMDigiCollection> digis;
  iEvent.getByLabel(label, digis);

  edm::ESHandle<GEMGeometry> gemGeom;
  iSetup.get<MuonGeometryRecord>().get(gemGeom);

  edm::ESHandle<MuonDetLayerGeometry> geo;
  iSetup.get<MuonRecoGeometryRecord>().get(geo);

  edm::Handle<GEMRecHitCollection> gemRecHits; 
  iEvent.getByLabel("gemRecHits","",gemRecHits);

  histContainer_["hGEMRecHitSize"]->Fill(gemRecHits->size());

  ESHandle<MagneticField> theMGField;
  iSetup.get<IdealMagneticFieldRecord>().get(theMGField);

  ESHandle<GlobalTrackingGeometry> theTrackingGeometry;
  iSetup.get<GlobalTrackingGeometryRecord>().get(theTrackingGeometry);

  Handle<SimTrackContainer> simTracks;
  iEvent.getByLabel("g4SimHits",simTracks);

  edm::Handle<edm::PSimHitContainer> GEMHits;
  iEvent.getByLabel(edm::InputTag("g4SimHits","MuonGEMHits"), GEMHits);

  for (GEMRecHitCollection::const_iterator recHit = gemRecHits->begin(); recHit != gemRecHits->end(); recHit++) {

	if (recHit->geographicalId().det() == DetId::Muon){

		if (recHit->geographicalId().subdetId() == MuonSubdetId::GEM){

			//std::cout<<"id: "<<GEMDetId(recHit->geographicalId().rawId())<<std::endl;
			numGemRecHits++;

		}

	}

  }

  int count = 0;
  GEMDigiCollection::DigiRangeIterator detUnitIt;
  for (detUnitIt = digis->begin(); detUnitIt != digis->end(); ++detUnitIt)
  {

       	std::vector<int> firedStrips;

	std::cout<<(*detUnitIt).first<<std::endl;
   	count++;

	GEMDigiCollection::const_iterator digiItr;
    	//loop over digis of given roll
    	for (digiItr = (*detUnitIt).second.first; digiItr != (*detUnitIt).second.second; ++digiItr)
    	{

    		GEMDetId id = (*detUnitIt).first; 
    		const GeomDet* gdet = gemGeom->idToDet(id);
    		const BoundPlane & surface = gdet->surface();
    		const GEMEtaPartition * roll = gemGeom->etaPartition(id);

		int strip = (int) digiItr->strip();
      		int bx = (int) digiItr->bx();

		firedStrips.push_back(strip);
		int nCluster = countCluster(firedStrips);

      		LocalPoint lp = roll->centreOfStrip(digiItr->strip());
      		double digi_x = (float) lp.x();
      		double digi_y = (float) lp.y();

      		GlobalPoint gp = surface.toGlobal(lp);
      		double digi_eta = (double) gp.eta();
     		double digi_phi = (double) gp.phi();
      		double digi_gx = (double) gp.x();
      		double digi_gy = (double) gp.y();
      		double digi_gz = (double) gp.z();

		std::cout<<strip<<" "<<bx<<" "<<digi_x<<" "<<digi_y<<std::endl;

		histContainer_["hGEMDigiStrip_all"]->Fill(strip);
		histContainer_["hGEMDigiBX_all"]->Fill(bx);
		histContainer_["hGEMDigiX_all"]->Fill(digi_x);
		histContainer_["hGEMDigiEta_all"]->Fill(digi_eta);
		histContainer_["hGEMDigiPhi_all"]->Fill(digi_phi);
		histContainer_["hGEMDigiGX_all"]->Fill(digi_gx);
		histContainer_["hGEMDigiGY_all"]->Fill(digi_gy);
		histContainer_["hGEMDigiGZ_all"]->Fill(digi_gz);

		histContainer2D_["hGEMDigiOccXY_all"]->Fill(digi_gx, digi_gy);
		histContainer2D_["hGEMDigiOccZY_all"]->Fill(digi_gz, sqrt(digi_gx*digi_gx + digi_gy*digi_gy));
		histContainer_["hGEMDigiCluster_all"]->Fill(nCluster);

	}

  }
  histContainer_["hGEMDigiSize"]->Fill(count);

  //std::cout<<"Num. GEMRechHits: "<<numGemRecHits<<" Num. CSCRecHits: "<<numCscRecHits<<std::endl; 

  SimTrackContainer::const_iterator simTrack;
  reco::TrackCollection::const_iterator staTrack;
  GEMRecHitCollection::const_iterator recHit;

  int numSimHitsPerEvt = 0;
  int numRecHitsPerEvt = 0;

  std::vector<GEMRecHit> matchedRecHits;
  std::vector<GlobalPoint> matchedRecHitsGP;
  std::vector<LocalPoint> matchedRecHitsLP;
  std::vector<int> matchedRecHitsStrip;

  for (recHit = gemRecHits->begin(); recHit != gemRecHits->end(); recHit++) {

	GEMDetId rollId = (GEMDetId)(*recHit).gemId();

	int region = rollId.region();
	//int layer = rollId.layer();
	//int chamber = rollId.chamber();

	histContainer_["hRecHitPerRegion"]->Fill(region);

  }

  for (edm::PSimHitContainer::const_iterator itHit = GEMHits->begin(); itHit != GEMHits->end(); ++itHit){

	DetId id = DetId(itHit->detUnitId());
	GEMDetId idGem = GEMDetId(itHit->detUnitId());

	int region_sim = idGem.region();
	int layer_sim = idGem.layer();
        int chamber_sim = idGem.chamber();
        //int roll_sim = idGem.roll();

	histContainer2D_["hSimHitVsType"]->Fill(itHit->particleType(), region_sim);
	histContainer_["hSimHitType"]->Fill(itHit->particleType());

      	LocalPoint lp = itHit->entryPoint();
	double x_sh = lp.x();
	double y_sh = lp.y();
      	int strip_sim = gemGeom->etaPartition(idGem)->strip(lp);

	if(itHit->particleType() == 13) histContainer_["hSimHitStripEle"]->Fill(strip_sim);
	if(itHit->particleType() == 11) histContainer_["hSimHitStripMu"]->Fill(strip_sim);

	if(itHit->particleType() != 13) continue;

	histContainer_["hSimHitChamber"]->Fill(chamber_sim);

	histContainer_["hSimHitLX"]->Fill(x_sh);
	histContainer_["hSimHitLY"]->Fill(y_sh);

	GlobalPoint pointSimHit = theTrackingGeometry->idToDetUnit(id)->toGlobal(itHit->localPosition());

	//float x_sim = itHit->localPosition().x();
	float simX = pointSimHit.x();
	float simY = pointSimHit.y();
	float simPhi = pointSimHit.phi();
	float simEta = pointSimHit.eta();
	//int stripNum_sim = itHit->firstClusterStrip();

	histContainer2D_["hSimHitOcc"]->Fill(simX, simY);

	numSimHitsPerEvt++;

    	for (detUnitIt = digis->begin(); detUnitIt != digis->end(); ++detUnitIt)
  	{

		GEMDigiCollection::const_iterator digiItr;
    		//loop over digis of given roll
    		for (digiItr = (*detUnitIt).second.first; digiItr != (*detUnitIt).second.second; ++digiItr)
    		{

	    		GEMDetId id = (*detUnitIt).first; 
	    		const GeomDet* gdet = gemGeom->idToDet(id);
	    		const BoundPlane & surface = gdet->surface();
	    		const GEMEtaPartition * roll = gemGeom->etaPartition(id);

    			int region = (int) id.region();
    			int layer = (int) id.layer();
    			int chamber = (int) id.chamber();

			int strip = (int) digiItr->strip();
	      		int bx = (int) digiItr->bx();

	      		LocalPoint lp = roll->centreOfStrip(digiItr->strip());
	      		double digi_x = (float) lp.x();
	      		//double digi_y = (float) lp.y();

	      		GlobalPoint gp = surface.toGlobal(lp);
	      		double digi_eta = (double) gp.eta();
	     		double digi_phi = (double) gp.phi();
	      		double digi_gx = (double) gp.x();
	      		double digi_gy = (double) gp.y();
	      		double digi_gz = (double) gp.z();

			//std::cout<<strip<<" "<<bx<<" "<<digi_x<<" "<<digi_y<<std::endl;

      			if(region != region_sim) continue;
      			if(layer != layer_sim) continue;
      			if(chamber != chamber_sim) continue;

      			if(abs(strip - strip_sim) > 2) continue;

			histContainer_["hGEMDigiStrip_match"]->Fill(strip);
			histContainer_["hGEMDigiBX_match"]->Fill(bx);
			histContainer_["hGEMDigiX_match"]->Fill(digi_x);
			histContainer_["hGEMDigiEta_match"]->Fill(digi_eta);
			histContainer_["hGEMDigiPhi_match"]->Fill(digi_phi);
			histContainer_["hGEMDigiGX_match"]->Fill(digi_gx);
			histContainer_["hGEMDigiGY_match"]->Fill(digi_gy);
			histContainer_["hGEMDigiGZ_match"]->Fill(digi_gz);

			histContainer2D_["hGEMDigiOccXY_match"]->Fill(digi_gx, digi_gy);
			histContainer2D_["hGEMDigiOccZY_match"]->Fill(digi_gz, sqrt(digi_gx*digi_gx + digi_gy*digi_gy));

		}

  	}

  	for (recHit = gemRecHits->begin(); recHit != gemRecHits->end(); recHit++) {

		GEMDetId rollId = (GEMDetId)(*recHit).gemId();
		LocalPoint recHitPos=recHit->localPosition();
		const GEMEtaPartition* rollasociated = gemGeom->etaPartition(rollId);
		const BoundPlane & GEMSurface = rollasociated->surface(); 
		GlobalPoint GEMGlobalPoint = GEMSurface.toGlobal(recHitPos);

		int cls = recHit->clusterSize();

		int region = rollId.region();
		int layer = rollId.layer();
		int chamber = rollId.chamber();
      		//int roll = rollId.roll();

		double x_rh = recHitPos.x();
		double y_rh = recHitPos.y();

		double x = GEMGlobalPoint.x();
		double y = GEMGlobalPoint.y();
		double z = GEMGlobalPoint.z();

		double recPhi = GEMGlobalPoint.phi();
		double recEta = GEMGlobalPoint.eta();
		double dR = deltaR(simEta, simPhi, recEta, recPhi);

		histContainer_["hDR"]->Fill(dR);

		if(!(region_sim == region && layer_sim == layer)) continue;
		if(dR > 0.1) continue;

		//if(!isMatched(strip_sim, recHit->firstClusterStrip(), cls)) continue;

		histContainer_["hCLS"]->Fill(cls);

		histContainer_["hRecHitLX"]->Fill(x_rh);
		histContainer_["hRecHitLY"]->Fill(y_rh);

		histContainer_["hRecHitPull"]->Fill(x_sh - x_rh);
		histContainer2D_["hRecHitRY"]->Fill(abs(z), sqrt(x*x + y*y));
		histContainer_["hRecHitEta"]->Fill(abs(recEta));
	 	histContainer_["hRecHitChamber"]->Fill(chamber);
		histContainer2D_["hRecHitOcc"]->Fill(x, y);
		numRecHitsPerEvt++;

		int stripNum = recHit->firstClusterStrip();
		//double x_reco = recHitPos.x();
		//float phi_02pi = recPhi < 0 ? recPhi + TMath::Pi() : recPhi;
		//float phiDeg = phi_02pi * 180/ TMath::Pi();

		//std::cout<<"Local x: "<<x_reco<<std::endl;
		//std::cout<<"Global x: "<<x<<" y: "<<y<<" z: "<<z<<std::endl;
		//std::cout<<"StripNumber: "<<stripNum<<std::endl;
		matchedRecHits.push_back(*recHit);
		matchedRecHitsGP.push_back(GEMGlobalPoint);
		matchedRecHitsLP.push_back(recHitPos);
		matchedRecHitsStrip.push_back(stripNum);

    	}

  }

  histContainer_["hSimHitMult"]->Fill(numSimHitsPerEvt);
  histContainer_["hRecHitMult"]->Fill(numRecHitsPerEvt);

  //std::cout<<"Num. GEMRechHitsSTA: "<<numGemRecHitsFromSTA<<" Num. CSCRecHitsSTA: "<<numCscRecHitsFromSTA<<std::endl; 

}


// ------------ method called once each job just before starting event loop  ------------
void 
GEMRecHitsReader::beginJob()
{

  edm::Service<TFileService> fs;
  histContainer_["hSimHitChamber"] = fs->make<TH1F>("SimHitChamber", "SimHitChamber", 36, 0, 36);
  histContainer_["hRecHitChamber"] = fs->make<TH1F>("RecHitChamber", "RecHitChamber", 36, 0, 36);

  histContainer_["hSimHitMult"] = fs->make<TH1F>("SimHitMult", "SimHitMult", 5, 0, 5);
  histContainer_["hRecHitMult"] = fs->make<TH1F>("RecHitMult", "RecHitMult", 5, 0, 5);

  histContainer_["hDR"] = fs->make<TH1F>("DR", "DR", 300, 0, 1);

  histContainer2D_["hSimHitOcc"] = fs->make<TH2F>("SimHitOcc", "SimHitOcc", 260, -260, 260, 260, -260, 260);
  histContainer2D_["hRecHitOcc"] = fs->make<TH2F>("RecHitOcc", "RecHitOcc", 260, -260, 260, 260, -260, 260);

  histContainer2D_["hSimHitVsType"] = fs->make<TH2F>("SimHitVsType", "SimHitVsType", 40, -20, 20, 5, -2.5, 2.5);
  histContainer_["hSimHitType"] = fs->make<TH1F>("SimHitType", "SimHitType", 501, -250.5, 250.5);
  histContainer_["hRecHitPerRegion"] = fs->make<TH1F>("RecHitVsType", "RecHitVsType", 5, -2.5, 2.5);

  histContainer_["hGEMRecHitSize"] = fs->make<TH1F>("GEMRecHitSize", "GEMRecHitSize", 100, 0, 100);
  histContainer_["hGEMDigiSize"] = fs->make<TH1F>("GEMDigiSize", "GEMDigiSize", 100, 0, 100);

  histContainer_["hGEMDigiStrip_all"] = fs->make<TH1F>("GEMDigiStrip_all", "GEMDigiStrip_all", 384, 0.5, 384.5);
  histContainer_["hGEMDigiBX_all"] = fs->make<TH1F>("GEMDigiBX_all", "GEMDigiBX_all", 21, -10.5, +10.5);
  histContainer_["hGEMDigiX_all"] = fs->make<TH1F>("GEMDigiX_all", "GEMDigiX_all", 61, -30.5, +30.5);

  histContainer_["hGEMDigiEta_all"] = fs->make<TH1F>("GEMDigiEta_all", "GEMDigiEta_all", 440, -2.2, +2.2);
  histContainer_["hGEMDigiPhi_all"] = fs->make<TH1F>("GEMDigiPhi_all", "GEMDigiPhi_all", 360, -TMath::Pi(), +TMath::Pi());
  histContainer_["hGEMDigiGX_all"] = fs->make<TH1F>("GEMDigiGX_all", "GEMDigiGX_all", 260, -260, 260);
  histContainer_["hGEMDigiGY_all"] = fs->make<TH1F>("GEMDigiGY_all", "GEMDigiGY_all", 55, 130, 240);
  histContainer_["hGEMDigiGZ_all"] = fs->make<TH1F>("GEMDigiGZ_all", "GEMDigiGZ_all", 400, -573, +573);

  histContainer2D_["hGEMDigiOccXY_all"] = fs->make<TH2F>("GEMDigiOccXY_all", "GEMDigiOccXY_all", 260, -260, 260, 260, -260, 260);
  histContainer2D_["hGEMDigiOccZY_all"] = fs->make<TH2F>("GEMDigiOccZY_all", "GEMDigiOccZY_all", 200, 564, 573, 110, 130, 240);

  histContainer_["hGEMDigiStrip_match"] = fs->make<TH1F>("GEMDigiStrip_match", "GEMDigiStrip_match", 384, 0.5, 384.5);
  histContainer_["hGEMDigiBX_match"] = fs->make<TH1F>("GEMDigiBX_match", "GEMDigiBX_match", 21, -10.5, +10.5);
  histContainer_["hGEMDigiX_match"] = fs->make<TH1F>("GEMDigiX_match", "GEMDigiX_match", 61, -30.5, +30.5);

  histContainer_["hGEMDigiEta_match"] = fs->make<TH1F>("GEMDigiEta_match", "GEMDigiEta_match", 440, -2.2, +2.2);
  histContainer_["hGEMDigiPhi_match"] = fs->make<TH1F>("GEMDigiPhi_match", "GEMDigiPhi_match", 360, -TMath::Pi(), +TMath::Pi());
  histContainer_["hGEMDigiGX_match"] = fs->make<TH1F>("GEMDigiGX_match", "GEMDigiGX_match", 260, -260, 260);
  histContainer_["hGEMDigiGY_match"] = fs->make<TH1F>("GEMDigiGY_match", "GEMDigiGY_match", 55, 130, 240);
  histContainer_["hGEMDigiGZ_match"] = fs->make<TH1F>("GEMDigiGZ_match", "GEMDigiGZ_match", 400, -573, +573);

  histContainer2D_["hGEMDigiOccXY_match"] = fs->make<TH2F>("GEMDigiOccXY_match", "GEMDigiOccXY_match", 260, -260, 260, 260, -260, 260);
  histContainer2D_["hGEMDigiOccZY_match"] = fs->make<TH2F>("GEMDigiOccZY_match", "GEMDigiOccZY_match", 200, 564, 573, 110, 130, 240);

  histContainer_["hSimHitLX"] = fs->make<TH1F>("SimHitLX", "SimHitLX", 61, -30.5, +30.5);
  histContainer_["hSimHitLY"] = fs->make<TH1F>("SimHitLY", "SimHitLY", 170, -8.5, 8.5);

  histContainer_["hRecHitLX"] = fs->make<TH1F>("RecHitLX", "RecHitLX", 61, -30.5, +30.5);
  histContainer_["hRecHitLY"] = fs->make<TH1F>("RecHitLY", "RecHitLY", 100, 0, 10);

  histContainer_["hRecHitPull"] = fs->make<TH1F>("RecHitPull", "RecHitPull", 200, -10, +10);

  histContainer_["hCLS"] = fs->make<TH1F>("CLS", "CLS", 11, -0.5, 10.5);
  histContainer_["hGEMDigiCluster_all"] = fs->make<TH1F>("GEMDigiCluster_all", "GEMDigiCluster_all", 21, -0.5, 20.5);

  histContainer_["hSimHitStripEle"] = fs->make<TH1F>("SimHitStripEle", "SimHitStripEle", 384, 0.5, 384.5);
  histContainer_["hSimHitStripMu"] = fs->make<TH1F>("SimHitStripMu", "SimHitStripMu", 384, 0.5, 384.5);

  histContainer_["hRecHitEta"] = fs->make<TH1F>("RecHitEta", "RecHitEta", 700, 1.5, 2.2);
  histContainer2D_["hRecHitRY"] = fs->make<TH2F>("RecHitRY", "RecHitRY", 200, 564, 573, 110, 130, 240);

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
