import FWCore.ParameterSet.Config as cms

process = cms.Process("GEMLocalRECO")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

#process.Timing = cms.Service("Timing")
process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )


# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.Geometry.GeometryExtended2019Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Digi_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgrade2019', '')


# Load GEM RecHit process
#########################
process.gemRecHits = cms.EDProducer("GEMRecHitProducer",
                                        recAlgoConfig = cms.PSet(),
                                        recAlgo = cms.string('GEMRecHitStandardAlgo'),
                                        gemDigiLabel = cms.InputTag("simMuonGEMDigis"),
                                        maskSource = cms.string('File'),
                                        maskvecfile = cms.FileInPath('RecoLocalMuon/GEMRecHit/data/GEMMaskVec.dat'),
                                        deadSource = cms.string('File'),
                                        deadvecfile = cms.FileInPath('RecoLocalMuon/GEMRecHit/data/GEMDeadVec.dat')
                                    )

### Input and Output Files
##########################
process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
    'file:step_GEM_DIGI.root'
    )
                            )

process.output = cms.OutputModule("PoolOutputModule",
                                      fileName = cms.untracked.string(
    'file:step_GEM_LocalReco.root'
    ),
                                      outputCommands = cms.untracked.vstring(
    'keep  *_*_*_*',
    ),
                                  SelectEvents = cms.untracked.PSet(
    SelectEvents = cms.vstring('rechit_step')
                )
                                  )

### Paths and Schedules
#######################
process.rechit_step    = cms.Path(process.gemRecHits)
process.endjob_step  = cms.Path(process.endOfProcess)
process.out_step     = cms.EndPath(process.output)


process.schedule = cms.Schedule(
        process.rechit_step,
            process.endjob_step,
            process.out_step
        )
