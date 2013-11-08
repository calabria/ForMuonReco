import FWCore.ParameterSet.Config as cms

process = cms.Process("STEP2")

process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2019Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("DQMServices.Components.EDMtoMEConverter_cfi")
process.load("DQMServices.Core.DQM_cfg")
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgrade2019', '')

process.load("DQMAnalyzer.DQMAnalyzerSTEP2.CfiFile_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

        'file:/cmshome/calabria/ProvaMelone2/CMSSW_6_2_0_SLHC1/src/DQMAnalyzer/DQMAnalyzerSTEP1/python/first_50GeV.root',
        'file:/cmshome/calabria/ProvaMelone2/CMSSW_6_2_0_SLHC1/src/DQMAnalyzer/DQMAnalyzerSTEP1/python/first_200GeV.root'

    )
)

process.p = cms.Path(process.EDMtoMEConverter * process.DQMGEMSecondStep)
process.DQM.collectorHost = ''
process.DQM.collectorPort = 9090
process.DQM.debug = False
