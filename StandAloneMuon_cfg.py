import FWCore.ParameterSet.Config as cms

process = cms.Process("RecoSTAMuon")
process.load("RecoMuon.Configuration.RecoMuon_cff")

process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2019Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgrade2019', '')

#--------------------------------------------------------------------------------

from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('python')
options.register ('includeGEMs',
                  True,
                  VarParsing.multiplicity.singleton,
                  VarParsing.varType.bool,
                  "Sample Type: True or False")

import sys
print sys.argv

if len(sys.argv) > 0:
    last = sys.argv.pop()
    sys.argv.extend(last.split(","))
    print sys.argv

if hasattr(sys, "argv") == True:
	options.parseArguments()
includeGEMs = options.includeGEMs
print 'Using includeGEMs: %s' % includeGEMs

#--------------------------------------------------------------------------------

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(

	#'file:/lustre/cms/store/relval/CMSSW_6_0_1_PostLS1v2_patch3-POSTLS161_V12/RelValZMM/GEN-SIM-RECO/v1/00000/4CC120BE-B03D-E211-8610-001A92810AA6.root'
	#'file:out_sim_digi.root'
	'file:./FileMarcello/step_GEM_LocalReco.root'

    )
)

#process.MessageLogger = cms.Service("MessageLogger",
#    cout = cms.untracked.PSet(
#        threshold = cms.untracked.string('INFO'),
#        noLineBreaks = cms.untracked.bool(True)
#    ),
#    destinations = cms.untracked.vstring('cout')
#)

process.out = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('RecoSTAMuons.root')
)

if includeGEMs:
	process.standAloneMuons.STATrajBuilderParameters.FilterParameters.EnableGEMMeasurement = cms.bool(True)
	process.standAloneMuons.STATrajBuilderParameters.BWFilterParameters.EnableGEMMeasurement = cms.bool(True)
else:
	process.standAloneMuons.STATrajBuilderParameters.FilterParameters.EnableGEMMeasurement = cms.bool(False)
	process.standAloneMuons.STATrajBuilderParameters.BWFilterParameters.EnableGEMMeasurement = cms.bool(False)

## Analyzer to produce pT and 1/pT resolution plots
process.STAMuonAnalyzer = cms.EDAnalyzer("STAMuonAnalyzer",
	DataType = cms.untracked.string('SimData'),
	StandAloneTrackCollectionLabel = cms.untracked.InputTag('standAloneMuons'),
	MuonSeedCollectionLabel = cms.untracked.string('standAloneMuonSeeds'),
	rootFileName = cms.untracked.string('STAMuonAnalyzer.root')
 	)

process.STAMuonAnalyzerWithGEMs = cms.EDAnalyzer("STAMuonAnalyzer",
	DataType = cms.untracked.string('SimData'),
	StandAloneTrackCollectionLabel = cms.untracked.InputTag('standAloneMuons','','RecoSTAMuon'),
	MuonSeedCollectionLabel = cms.untracked.string('standAloneMuonSeeds'),
	rootFileName = cms.untracked.string('STAMuonAnalyzerWithGEMs.root')
	)

process.demo = cms.EDAnalyzer('GEMRecHitsReader',
	simHit = cms.untracked.InputTag("g4SimHits", "MuonGEMHits"),
	recHit = cms.untracked.InputTag("gemRecHits"),
	simTrack = cms.untracked.InputTag("mix", "MergedTrackTruth"),
	staTrack = cms.untracked.InputTag("standAloneMuons"),
)

process.demoWithGEMs = cms.EDAnalyzer('GEMRecHitsReader',
	simHit = cms.untracked.InputTag("g4SimHits", "MuonGEMHits"),
	recHit = cms.untracked.InputTag("gemRecHits"),
	simTrack = cms.untracked.InputTag("mix", "MergedTrackTruth"),
	staTrack = cms.untracked.InputTag("standAloneMuons","","RecoSTAMuon"),
)

#process.MessageLogger = cms.Service("MessageLogger",
#       destinations = cms.untracked.vstring(                            #1
#                                             'myDebugOutputFile'        #2
#       ),
#       myDebugOutputFile = cms.untracked.PSet(                          #3
#                       threshold = cms.untracked.string('DEBUG'),       #4
#                       default = cms.untracked.PSet(                   
#                       		limit = cms.untracked.int32(-1)  #5
#        	       ),
#       debugModules = cms.untracked.vstring(                            #6
#                      'standAloneMuons'
#	)                                                                #7
#       )                                                                #8
#)

if includeGEMs:
	process.p = cms.Path(process.standAloneMuons * process.STAMuonAnalyzerWithGEMs * process.demoWithGEMs)
else:
	process.p = cms.Path(process.standAloneMuons * process.STAMuonAnalyzer * process.demo)

process.this_is_the_end = cms.EndPath(process.out)
