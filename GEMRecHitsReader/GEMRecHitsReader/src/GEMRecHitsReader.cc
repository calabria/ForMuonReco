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

  edm::ESHandle<MagneticField> magfield;
  iSetup.get<IdealMagneticFieldRecord>().get(magfield);

  edm::Handle<GEMRecHitCollection> gemRecHits; 
  iEvent.getByLabel("gemRecHits","",gemRecHits);

  edm::Handle<CSCRecHit2DCollection> cscRecHits; 
  iEvent.getByLabel("csc2DRecHits","",cscRecHits);

  Handle<reco::TrackCollection> staTracks;
  iEvent.getByLabel(staTrackLabel_, staTracks);

  std::cout<<"input "<<staTrackLabel_<<std::endl;

  ESHandle<MagneticField> theMGField;
  iSetup.get<IdealMagneticFieldRecord>().get(theMGField);

  ESHandle<GlobalTrackingGeometry> theTrackingGeometry;
  iSetup.get<GlobalTrackingGeometryRecord>().get(theTrackingGeometry);

  Handle<SimTrackContainer> simTracks;
  iEvent.getByLabel("g4SimHits",simTracks);

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


  std::cout<<"Num. GEMRechHits: "<<numGemRecHits<<" Num. CSCRecHits: "<<numCscRecHits<<std::endl; 


  SimTrackContainer::const_iterator simTrack;
  reco::TrackCollection::const_iterator staTrack;

  for (reco::TrackCollection::const_iterator staTrack = staTracks->begin(); staTrack != staTracks->end(); ++staTrack){

    	reco::TransientTrack track(*staTrack,&*theMGField,theTrackingGeometry); 

    	for(trackingRecHit_iterator recHit = staTrack->recHitsBegin(); recHit != staTrack->recHitsEnd(); ++recHit){

      		const GeomDet* geomDet = theTrackingGeometry->idToDet((*recHit)->geographicalId());
      		double r = geomDet->surface().position().perp();
      		double z = geomDet->toGlobal((*recHit)->localPosition()).z();
      		double x = geomDet->toGlobal((*recHit)->localPosition()).x();
      		double y = geomDet->toGlobal((*recHit)->localPosition()).y();
      		std::cout<<"x: "<<x<<" y: "<<y<<" r: "<< r <<" z: "<<z<<std::endl;


		if ((*recHit)->geographicalId().det() == DetId::Muon){

			if ((*recHit)->geographicalId().subdetId() == MuonSubdetId::CSC){

				std::cout<<"CSC id: "<<CSCDetId((*recHit)->geographicalId().rawId())<<std::endl;
				numCscRecHitsFromSTA++;

			}

		}

		if ((*recHit)->geographicalId().det() == DetId::Muon){

			if ((*recHit)->geographicalId().subdetId() == MuonSubdetId::GEM){

				std::cout<<"GEM id: "<<GEMDetId((*recHit)->geographicalId().rawId())<<std::endl;
				numGemRecHitsFromSTA++;

			}

		}


    	}

  }

  std::cout<<"Num. GEMRechHitsSTA: "<<numGemRecHitsFromSTA<<" Num. CSCRecHitsSTA: "<<numCscRecHitsFromSTA<<std::endl; 

}


// ------------ method called once each job just before starting event loop  ------------
void 
GEMRecHitsReader::beginJob()
{
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
