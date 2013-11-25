import FWCore.ParameterSet.Config as cms
import os

process = cms.Process("DQM1")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1)
)
process.source = cms.Source("EmptySource")

CMSSW_BASE       = os.environ['CMSSW_BASE']
pathForSaving    = "/lustre/cms/store/user/calabria/DQMGem/"
pathCFGLocation  = CMSSW_BASE + "/src/DQMAnalyzer/DQMAnalyzerSTEP1/python/"
fileLocation     = CMSSW_BASE + "/src/WHAnalysis/BatchSubmission/TXTFiles/GEM/liste_sampleGEM/"
channel          = "DQM"
cshTemp          = "batchJob_cmssusy.csh"

process.SingleMuPt5 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("ConfFile_cfi_temp.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("SingleMuPt5"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation + "5GeV_GEM.txt"),
	folderDQM = cms.untracked.string("GEMBasicPlots/SingleMu5GeV")

)

process.SingleMuPt10 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("ConfFile_cfi_temp.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("SingleMuPt10"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation + "10GeV_GEM.txt"),
	folderDQM = cms.untracked.string("GEMBasicPlots/SingleMu10GeV")

)

process.SingleMuPt50 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("ConfFile_cfi_temp.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("SingleMuPt50"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation + "50GeV_GEM.txt"),
	folderDQM = cms.untracked.string("GEMBasicPlots/SingleMu50GeV")

)

process.SingleMuPt100 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("ConfFile_cfi_temp.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("SingleMuPt100"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation + "100GeV_GEM.txt"),
	folderDQM = cms.untracked.string("GEMBasicPlots/SingleMu100GeV")

)

process.SingleMuPt200 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("ConfFile_cfi_temp.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("SingleMuPt200"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation + "200GeV_GEM.txt"),
	folderDQM = cms.untracked.string("GEMBasicPlots/SingleMu200GeV")

)

process.SingleMuPt500 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("ConfFile_cfi_temp.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("SingleMuPt500"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation + "500GeV_GEM.txt"),
	folderDQM = cms.untracked.string("GEMBasicPlots/SingleMu500GeV")

)

process.SingleMuPt1000 = cms.EDAnalyzer('BatchSubmission',

	finalState = cms.untracked.string(channel),
	fileCFG = cms.untracked.string("ConfFile_cfi_temp.py"),
	fileCSH = cms.untracked.string(cshTemp),

	sample = cms.untracked.string("SingleMuPt1000"),
	pathCFG = cms.untracked.string(pathCFGLocation),
	savingPath = cms.untracked.string(pathForSaving),
	txtFile = cms.untracked.string(fileLocation + "1000GeV_GEM.txt"),
	folderDQM = cms.untracked.string("GEMBasicPlots/SingleMu1000GeV")

)

process.p = cms.Path(
	process.SingleMuPt5 +
	process.SingleMuPt10 +
	process.SingleMuPt50 +
	process.SingleMuPt100 + 
	process.SingleMuPt200 + 
	process.SingleMuPt500 + 
	process.SingleMuPt1000
)
