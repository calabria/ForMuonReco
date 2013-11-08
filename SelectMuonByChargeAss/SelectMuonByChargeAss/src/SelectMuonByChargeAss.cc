// -*- C++ -*-
//
// Package:    SelectMuonByChargeAss
// Class:      SelectMuonByChargeAss
// 
/**\class SelectMuonByChargeAss SelectMuonByChargeAss.cc SelectMuonByChargeAss/SelectMuonByChargeAss/src/SelectMuonByChargeAss.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Cesare Calabria
//         Created:  Sun Sep 29 12:18:14 CEST 2013
// $Id$
//
//

// Base Class Headers
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDFilter.h"
#include <FWCore/Framework/interface/EventSetup.h>
#include <FWCore/Framework/interface/ESHandle.h>
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

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

#include "TrackingTools/GeomPropagators/interface/Propagator.h"
#include "SimDataFormats/Vertex/interface/SimVertexContainer.h"
#include "DataFormats/GeometrySurface/interface/Plane.h"
#include "TrackingTools/Records/interface/TrackingComponentsRecord.h"

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

#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

using namespace std;
using namespace edm;

//
// class declaration
//

class SelectMuonByChargeAss : public edm::EDFilter {
   public:
      explicit SelectMuonByChargeAss(const edm::ParameterSet&);
      ~SelectMuonByChargeAss();

      static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

   private:
      virtual void beginJob() ;
      virtual bool filter(edm::Event&, const edm::EventSetup&);
      virtual void endJob() ;
      
      //virtual bool beginRun(edm::Run&, edm::EventSetup const&);
      //virtual bool endRun(edm::Run&, edm::EventSetup const&);
      //virtual bool beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);
      //virtual bool endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&);

      // ----------member data ---------------------------

      edm::InputTag staTrackLabel_;
      edm::InputTag staTrackGemLabel_;

      std::map<std::string,TH1F*> histContainer_;
      std::map<std::string,TH2F*> histContainer2D_; 

      int numSTDMuons = 0;
      int numGEMMuons = 0;
      int numSelMuons = 0;

};

bool isSimMatched(SimTrackContainer::const_iterator simTrack, edm::PSimHitContainer::const_iterator itHit)
{

  bool result = false;

  int trackId = simTrack->trackId();
  int trackId_sim = itHit->trackId();
  if(trackId == trackId_sim) result = true;

  //std::cout<<"ID: "<<trackId<<" "<<trackId_sim<<" "<<result<<std::endl;

  return result;

}

edm::PSimHitContainer isTrackMatched(SimTrackContainer::const_iterator simTrack, const Event & event, const EventSetup& eventSetup)
{

  edm::PSimHitContainer selectedGEMHits;

  //GlobalPoint gbTemp = propagatedPositionGEM(simTrack, event, eventSetup);
  //std::cout<<gbTemp.x()<<std::endl;

  edm::Handle<edm::PSimHitContainer> GEMHits;
  event.getByLabel(edm::InputTag("g4SimHits","MuonGEMHits"), GEMHits);

  ESHandle<GlobalTrackingGeometry> theTrackingGeometry;
  eventSetup.get<GlobalTrackingGeometryRecord>().get(theTrackingGeometry);

  for (edm::PSimHitContainer::const_iterator itHit = GEMHits->begin(); itHit != GEMHits->end(); ++itHit){
							 
	DetId id = DetId(itHit->detUnitId());
	if (!(id.subdetId() == MuonSubdetId::GEM)) continue;
  	if(itHit->particleType() != (*simTrack).type()) continue;

	bool result = isSimMatched(simTrack, itHit);
	if(result) selectedGEMHits.push_back(*itHit);

  }

  //std::cout<<"Size: "<<selectedGEMHits.size()<<std::endl;
  return selectedGEMHits;

}

bool isRecHitMatched(edm::PSimHitContainer selGEMSimHits, trackingRecHit_iterator recHit, edm::ESHandle<GEMGeometry> gemGeom)
{
 
  bool result = false;

  GEMDetId id((*recHit)->geographicalId());
  LocalPoint lp1 = (*recHit)->localPosition();
  int region = id.region();
  int layer = id.layer();
  int chamber = id.chamber();
  int roll = id.roll();
  int strip = gemGeom->etaPartition(id)->strip(lp1);
 
  for(edm::PSimHitContainer::const_iterator itHit = selGEMSimHits.begin(); itHit != selGEMSimHits.end(); ++itHit){

      	GEMDetId idGem = GEMDetId(itHit->detUnitId());
      	int region_sim = idGem.region();
      	int layer_sim = idGem.layer();
      	int chamber_sim = idGem.chamber();
      	int roll_sim = idGem.roll();

      	LocalPoint lp = itHit->entryPoint();
      	int strip_sim = gemGeom->etaPartition(idGem)->strip(lp);

	//std::cout<<"Strip: "<<strip<<" "<<strip_sim<<std::endl;

      	if(region != region_sim) continue;
      	if(layer != layer_sim) continue;
      	if(chamber != chamber_sim) continue;
      	if(roll != roll_sim) continue;

      	if(abs(strip - strip_sim) < 2) result = true;

  }

  //std::cout<<"RecHit: "<<result<<std::endl;
  return result;

}

//
// constants, enums and typedefs
//

//
// static data member definitions
//

//
// constructors and destructor
//
SelectMuonByChargeAss::SelectMuonByChargeAss(const edm::ParameterSet& iConfig):
  histContainer_(),
  histContainer2D_()
{
   //now do what ever initialization is needed

  staTrackLabel_ = iConfig.getUntrackedParameter<edm::InputTag>("StandAloneTrackCollectionLabel");
  staTrackGemLabel_ = iConfig.getUntrackedParameter<edm::InputTag>("StandAloneGemTrackCollectionLabel");

  produces<reco::TrackCollection>("");

}


SelectMuonByChargeAss::~SelectMuonByChargeAss()
{
 
   // do anything here that needs to be done at desctruction time
   // (e.g. close files, deallocate resources etc.)

}


//
// member functions
//

// ------------ method called on each new Event  ------------
bool
SelectMuonByChargeAss::filter(edm::Event& iEvent, const edm::EventSetup& iSetup)
{
  
  // Get the RecTrack collection from the event
  Handle<reco::TrackCollection> staTracks;
  iEvent.getByLabel(staTrackLabel_, staTracks);

  Handle<reco::TrackCollection> staTracksGem;
  iEvent.getByLabel(staTrackGemLabel_, staTracksGem);

  Handle<SimTrackContainer> simTracks;
  iEvent.getByLabel("g4SimHits",simTracks);

  ESHandle<MagneticField> theMGField;
  iSetup.get<IdealMagneticFieldRecord>().get(theMGField);

  edm::ESHandle<GEMGeometry> gemGeom;
  iSetup.get<MuonGeometryRecord>().get(gemGeom);

  edm::ESHandle<MuonDetLayerGeometry> geo;
  iSetup.get<MuonRecoGeometryRecord>().get(geo);

  ESHandle<GlobalTrackingGeometry> theTrackingGeometry;
  iSetup.get<GlobalTrackingGeometryRecord>().get(theTrackingGeometry);

  edm::Handle<GEMRecHitCollection> gemRecHits; 
  iEvent.getByLabel("gemRecHits","",gemRecHits);

  edm::Handle<CSCRecHit2DCollection> cscRecHits; 
  iEvent.getByLabel("csc2DRecHits","",cscRecHits);

  edm::Handle<edm::PSimHitContainer> GEMHits;
  iEvent.getByLabel(edm::InputTag("g4SimHits","MuonGEMHits"), GEMHits);

  edm::Handle<edm::PSimHitContainer> CSCHits;
  iEvent.getByLabel(edm::InputTag("g4SimHits","MuonCSCHits"), CSCHits);

  SimTrackContainer::const_iterator simTrack;
  reco::TrackCollection::const_iterator staTrack;
  reco::TrackCollection::const_iterator staTrackGem;

  std::auto_ptr< reco::TrackCollection > selectedTracks( new reco::TrackCollection() );

  bool result = false;

  for (simTrack = simTracks->begin(); simTrack != simTracks->end(); ++simTrack){

	double simEta = (*simTrack).momentum().eta();
	double simPhi = (*simTrack).momentum().phi();
	double simPt = (*simTrack).momentum().pt();

	if (abs((*simTrack).type()) != 13) continue;
	if ((*simTrack).noVertex()) continue;
	if ((*simTrack).noGenpart()) continue;

	if (abs(simEta) > 2.1 || abs(simEta) < 1.64) continue;

	edm::PSimHitContainer matchedSimHits = isTrackMatched(simTrack, iEvent, iSetup);
	if(matchedSimHits.size() == 0) continue;

	int qSim = simTrack->charge();

	cout<<"SimPt: "<<simPt<<" SimEta "<<simEta<<" SimPhi "<<simPhi<<std::endl;

	bool exist = false;
	bool existGEM = false;
	bool existReduced = false;
	reco::TrackCollection standardTracks;

	for (staTrack = staTracks->begin(); staTrack != staTracks->end(); ++staTrack){

		double recPtSTD = staTrack->pt();;

		double recEtaSTD = staTrack->momentum().eta();
		double recPhiSTD = staTrack->momentum().phi();

		double dRSTD = sqrt(pow((simEta-recEtaSTD),2) + pow((simPhi-recPhiSTD),2));

		histContainer_["hDRSTD"]->Fill(dRSTD);
		if(dRSTD > 0.1) continue;
		if(!(recPtSTD && abs(recEtaSTD) > 1.64 && abs(recEtaSTD) < 2.1)) continue;

		int qRecSTD = staTrack->charge();
		int deltaQ = abs(qSim - qRecSTD);

		if(deltaQ != 2) continue;

		exist = true;	
		numSTDMuons++;
		standardTracks.push_back(*staTrack);

		cout<<"RecPtSTD "<<recPtSTD<<" RecEtaSTD "<<recEtaSTD<<" recPhiSTD "<<recPhiSTD<<std::endl;
		std::cout<<"NOGEM: "<<qSim<<" "<<qRecSTD<<" "<<deltaQ<<std::endl;
		cout<<"dRSTD "<<dRSTD<<std::endl;

	}

	for (staTrackGem = staTracksGem->begin(); staTrackGem != staTracksGem->end(); ++staTrackGem){

		double recPt = staTrackGem->pt();;

		double recEta = staTrackGem->momentum().eta();
		double recPhi = staTrackGem->momentum().phi();

		double dR = sqrt(pow((simEta-recEta),2) + pow((simPhi-recPhi),2));

		histContainer_["hDR"]->Fill(dR);
		if(dR > 0.1) continue;
		if(!(recPt && abs(recEta) > 1.64 && abs(recEta) < 2.1)) continue;

		std::vector<bool> hasGemRecHits;

		for(trackingRecHit_iterator recHit = staTrackGem->recHitsBegin(); recHit != staTrackGem->recHitsEnd(); ++recHit){

			if (!((*recHit)->geographicalId().det() == DetId::Muon)) continue;
			if (!((*recHit)->geographicalId().subdetId() == MuonSubdetId::GEM)) continue;

			hasGemRecHits.push_back(isRecHitMatched(matchedSimHits, recHit, gemGeom));

		}

		if(hasGemRecHits.size() == 0) continue;

		/*bool allRHMatched = true;
		bool parRHMatched = false;

		for(int i=0; i<(int)hasGemRecHits.size(); i++){

			std::cout<<hasGemRecHits[i]<<std::endl;
			allRHMatched &= hasGemRecHits[i];
			parRHMatched |= hasGemRecHits[i];

		}

		if(!allRHMatched) continue;*/

		int qRecGem = staTrackGem->charge();
		int deltaQGem = abs(qSim - qRecGem);

		if(deltaQGem != 0) continue;
		
		existGEM = true;
		numGEMMuons++;

  		reco::TrackCollection::const_iterator staTrack2;
		for (staTrack2 = standardTracks.begin(); staTrack2 != standardTracks.end(); ++staTrack2){

			double recPtSTD = staTrack2->pt();;

			double recEtaSTD = staTrack2->momentum().eta();
			double recPhiSTD = staTrack2->momentum().phi();

			double dRSTD = sqrt(pow((recEta-recEtaSTD),2) + pow((recPhi-recPhiSTD),2));

			histContainer_["hDR12"]->Fill(dRSTD);
			if(dRSTD > 0.1) continue;
			if(!(recPtSTD && abs(recEtaSTD) > 1.64 && abs(recEtaSTD) < 2.1)) continue;

			int qRecSTD = staTrack2->charge();
			int deltaQ = abs(qSim - qRecSTD);

			if(deltaQ*deltaQGem > 0) continue;

			existReduced = true;

		}

		if(existReduced) numSelMuons++;

		cout<<"RecPt: "<<recPt<<" RecEta "<<recEta<<" recPhi "<<recPhi<<std::endl;
		std::cout<<"GEM: "<<qSim<<" "<<qRecGem<<" "<<deltaQGem<<std::endl;
		cout<<"dR "<<dR<<std::endl;

	}

	std::cout<<"Final result: "<<exist<<" "<<existGEM<<" "<<existReduced<<std::endl;
	if(!(exist && existGEM && existReduced)) continue;

	result = true;
	//selectedTracks->push_back(*staTrackGem);

	std::cout<<"--------------------------------"<<std::endl;

  }

  iEvent.put( selectedTracks );
  return result;

}

// ------------ method called once each job just before starting event loop  ------------
void 
SelectMuonByChargeAss::beginJob()
{

  edm::Service<TFileService> fs;
  histContainer_["hDR"] = fs->make<TH1F>("DR", "DR", 300, 0, 0.01);
  histContainer_["hDRSTD"] = fs->make<TH1F>("DRSTD", "DRSTD", 300, 0, 0.01);
  histContainer_["hDR12"] = fs->make<TH1F>("DR12", "DR12", 300, 0, 0.1);

}

// ------------ method called once each job just after ending the event loop  ------------
void 
SelectMuonByChargeAss::endJob() {

  std::cout<<"STDMuons: "<<numSTDMuons<<" GEMMuons: "<<numGEMMuons<<" SelMuons: "<<numSelMuons<<std::endl;

}

// ------------ method called when starting to processes a run  ------------
/*
bool
SelectMuonByChargeAss::beginRun(edm::Run&, edm::EventSetup const&)
{ 
  return true;
}
*/
 
// ------------ method called when ending the processing of a run  ------------
/*
bool
SelectMuonByChargeAss::endRun(edm::Run&, edm::EventSetup const&)
{
  return true;
}
*/
 
// ------------ method called when starting to processes a luminosity block  ------------
/*
bool
SelectMuonByChargeAss::beginLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}
*/
 
// ------------ method called when ending the processing of a luminosity block  ------------
/*
bool
SelectMuonByChargeAss::endLuminosityBlock(edm::LuminosityBlock&, edm::EventSetup const&)
{
  return true;
}
*/
 
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
SelectMuonByChargeAss::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
  //The following says we do not know what parameters are allowed so do no validation
  // Please change this to state exactly what you do use, even if it is no parameters
  edm::ParameterSetDescription desc;
  desc.setUnknown();
  descriptions.addDefault(desc);
}
//define this as a plug-in
DEFINE_FWK_MODULE(SelectMuonByChargeAss);
