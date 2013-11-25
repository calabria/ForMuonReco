import FWCore.ParameterSet.Config as cms

process = cms.Process("STEP1")

process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2019Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff') #!!!!!!!!!!!!!!!!!!!!!!!!!!
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("DQMServices.Components.MEtoEDMConverter_cfi")
process.load("DQMServices.Core.DQM_cfg")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgrade2019', '')

process.GLBMuonAnalyzerWithGEMs = cms.EDAnalyzer("DQMAnalyzerSTEP1",
	StandAloneTrackCollectionLabel = cms.untracked.InputTag('globalMuons','','RECO'),
	MuonSeedCollectionLabel = cms.untracked.string('standAloneMuonSeeds'),
	debug = cms.untracked.bool(False),
	folderPath = cms.untracked.string(

		#__folderPath

        ),
	NoGEMCase = cms.untracked.bool(False),
	isGlobalMuon = cms.untracked.bool(True),
	EffSaveRootFile = cms.untracked.bool(True),
	EffRootFileName = cms.untracked.string(

		#__rootFile

	)
)

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

		#__inputFile

    )
)

process.FEVT = cms.OutputModule("PoolOutputModule",
    outputCommands = cms.untracked.vstring('keep *_MEtoEDMConverter_*_*'),
    fileName = cms.untracked.string(	

		#__outpuFile

    )
)

process.p = cms.Path(process.GLBMuonAnalyzerWithGEMs * process.MEtoEDMConverter)
process.outpath = cms.EndPath(process.FEVT)

process.DQM.collectorHost = ''
process.DQM.collectorPort = 9090
process.DQM.debug = False
