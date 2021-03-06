import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source("EmptySource")

process.demo = cms.EDAnalyzer('TestDetLayer')

process.load("Geometry.CSCGeometry.cscGeometry_cfi")
process.load("Geometry.DTGeometry.dtGeometry_cfi")
process.load("Geometry.RPCGeometry.rpcGeometry_cfi")

process.load("Configuration.StandardSequences.Services_cff")
process.load("Configuration.StandardSequences.Geometry_cff")
process.load("Geometry.GEMGeometry.gemGeometry_cfi")

process.load("Configuration.StandardSequences.MagneticField_38T_cff")
#process.load("MagneticField.Engine.volumeBasedMagneticField_cfi")

#process.load("Geometry.MuonCommonData.muonIdealGeometryXML_cfi")
process.load("Geometry.GEMGeometry.cmsExtendedGeometryPostLS1plusGEMXML_cfi")
process.load("RecoMuon.DetLayers.muonDetLayerGeometry_cfi")
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.GlobalTag.globaltag = 'MC_60_V7::All'
process.p = cms.Path(process.demo)

