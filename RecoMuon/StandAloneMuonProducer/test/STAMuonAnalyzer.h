#ifndef RecoMuon_StandAloneMuonProducer_STAMuonAnalyzer_H
#define RecoMuon_StandAloneMuonProducer_STAMuonAnalyzer_H

/** \class STAMuonAnalyzer
 *  Analyzer of the StandAlone muon tracks
 *
 *  $Date: 2009/10/31 05:19:45 $
 *  $Revision: 1.3 $
 *  \author R. Bellan - INFN Torino <riccardo.bellan@cern.ch>
 */

// Base Class Headers
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include <FWCore/Framework/interface/EventSetup.h>
#include <FWCore/Framework/interface/ESHandle.h>
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"

namespace edm {
  class ParameterSet;
  class Event;
  class EventSetup;
}

class TFile;
class TH1F;
class TH2F;

class STAMuonAnalyzer: public edm::EDAnalyzer {
public:
  /// Constructor
  STAMuonAnalyzer(const edm::ParameterSet& pset);

  /// Destructor
  virtual ~STAMuonAnalyzer();

  // Operations

  void analyze(const edm::Event & event, const edm::EventSetup& eventSetup);

  virtual void beginJob() ;
  virtual void endJob() ;
protected:

private:
  std::string theRootFileName;
  TFile* theFile;

  edm::InputTag staTrackLabel_;
  std::string theSeedCollectionLabel;
  bool noGEMCase_;

  // Histograms
  TH1F *hPtRec;
  TH1F *hPtSim; 
  TH1F *hPres;
  TH1F *h1_Pres;
  TH1F *hPTDiff;
  TH1F *hPTDiff2;
  TH2F *hPTDiffvsEta;
  TH2F *hPTDiffvsPhi;
  TH1F *hSimEta;
  TH1F *hRecEta;
  TH1F *hDeltaEta;
  TH1F *hDeltaPhi;
  TH1F *hSimPhi;
  TH1F *hRecPhi;
  TH1F *hNumSimTracks;
  TH1F *hNumMuonSimTracks;
  TH1F *hNumRecTracks;
  TH2F *hPtResVsPt;
  TH2F *hInvPtResVsPt;
  TH2F *hDPhiVsPt;
  TH1F *hDenPt;
  TH1F *hDenEta;
  TH1F *hNumPt;
  TH1F *hNumEta;
  TH1F *hPullGEM;
  TH1F *hPullCSC;
  TH1F *hGEMRecHitEta;
  TH1F *hDR;

  // Counters
  int numberOfSimTracks;
  int numberOfRecTracks;

  std::string theDataType;
  
};
#endif

