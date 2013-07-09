import FWCore.ParameterSet.Config as cms

process = cms.Process("RecoSTAMuon")
process.load("RecoMuon.Configuration.RecoMuon_cff")

process.load("Configuration.StandardSequences.MagneticField_cff")
#process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Geometry.GEMGeometry.cmsExtendedGeometryPostLS1plusGEMXML_cfi")
process.load("RecoMuon.DetLayers.muonDetLayerGeometry_cfi")
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("Configuration.StandardSequences.GeometryRecoDB_cff")

process.load("RecoLocalMuon.Configuration.RecoLocalMuon_cff")

process.dt1DRecHits.dtDigiLabel = cms.InputTag("simMuonDTDigis")
process.csc2DRecHits.wireDigiTag = cms.InputTag("simMuonCSCDigis","MuonCSCWireDigi")
process.csc2DRecHits.stripDigiTag = cms.InputTag("simMuonCSCDigis","MuonCSCStripDigi")
process.rpcRecHits.rpcDigiLabel = cms.InputTag("simMuonRPCDigis")

process.GlobalTag.globaltag = 'DESIGN60_V7::All'

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10)
)
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(

	#'file:/lustre/cms/store/relval/CMSSW_6_0_1_PostLS1v2_patch3-POSTLS161_V12/RelValZMM/GEN-SIM-RECO/v1/00000/4CC120BE-B03D-E211-8610-001A92810AA6.root'
	'file:/lustre/cms/store/user/calabria/out_sim_digi_10k.root'

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

process.dtlocalreco = cms.Sequence(process.dt1DRecHits*process.dt4DSegments)

## Analyzer to produce pT and 1/pT resolution plots
#process.STAMuonAnalyzer = cms.EDAnalyzer("STAMuonAnalyzer",
#                                         DataType = cms.untracked.string('SimData'),
#                                         StandAloneTrackCollectionLabel = cms.untracked.string('standAloneMuons'),
#                                         MuonSeedCollectionLabel = cms.untracked.string('MuonSeed'),
#                                         rootFileName = cms.untracked.string('STAMuonAnalyzer.root')
#                                         )

#process.p = cms.Path( process.standAloneMuonSeeds * process.standAloneMuons)                             ## default path (no analyzer)
process.p = cms.Path(process.muonlocalreco)
#process.p = cms.Path(process.MuonSeed * process.standAloneMuons * process.STAMuonAnalyzer)  ## path with analyzer
process.this_is_the_end = cms.EndPath(process.out)
