import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.Geometry.GeometryExtended2019Reco_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load('Configuration.StandardSequences.Reconstruction_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')
process.load("Geometry.GEMGeometry.gemGeometry_cfi")
process.load("Geometry.RPCGeometry.rpcGeometry_cfi")
process.load("Geometry.CSCGeometry.cscGeometry_cfi")
process.load("Geometry.DTGeometry.dtGeometry_cfi")
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi")

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgrade2019', '')

## GEM geometry customization
mynum = process.XMLIdealGeometryESSource.geomXMLFiles.index('Geometry/MuonCommonData/data/v4/gemf.xml')
process.XMLIdealGeometryESSource.geomXMLFiles.remove('Geometry/MuonCommonData/data/v4/gemf.xml')
process.XMLIdealGeometryESSource.geomXMLFiles.insert(mynum,'Geometry/MuonCommonData/data/v3/gemf.xml')

mynum = process.XMLIdealGeometryESSource.geomXMLFiles.index('Geometry/GEMGeometryBuilder/data/v4/GEMSpecs.xml')
process.XMLIdealGeometryESSource.geomXMLFiles.remove('Geometry/GEMGeometryBuilder/data/v4/GEMSpecs.xml')
process.XMLIdealGeometryESSource.geomXMLFiles.insert(mynum,'Geometry/GEMGeometryBuilder/data/v3/GEMSpecs.xml')

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(

	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_100_1_NXp.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_10_1_Lyn.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_11_1_xDR.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_12_3_adW.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_13_3_yUC.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_14_2_6Yl.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_15_3_6yH.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_16_2_ucQ.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_17_1_FQq.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_18_1_sdL.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_19_1_dW9.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_1_2_ueC.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_20_1_4CY.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_21_3_cxy.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_22_3_H0C.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_23_1_SJh.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_24_1_Jqx.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_25_1_cSR.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_26_1_2v8.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_27_1_D38.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_28_1_8fK.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_29_1_mzW.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_2_2_gbi.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_30_1_YQ6.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_31_1_OpA.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_32_1_nm7.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_33_1_Stv.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_34_1_B5Z.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_35_3_9kx.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_36_1_cTT.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_37_1_Rua.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_38_1_i7H.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_39_1_rro.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_3_2_9yd.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_40_1_3Wp.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_41_1_GID.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_42_1_YgQ.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_43_1_GsS.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_44_1_GsS.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_45_1_9Wm.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_46_1_LBe.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_47_1_NSz.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_48_1_GiV.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_49_1_HIq.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_4_1_PXM.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_50_3_NKc.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_51_1_FhC.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_52_1_1xw.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_53_1_Xp2.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_54_1_QtJ.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_55_1_Og9.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_56_3_Rw5.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_57_1_dCy.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_58_1_ity.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_59_1_8wC.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_5_2_Hxb.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_60_1_vgp.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_61_1_689.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_62_1_fzf.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_63_1_Bk1.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_64_1_jqh.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_65_1_UXY.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_66_1_BPQ.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_67_1_vAJ.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_68_1_RlI.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_69_1_kOe.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_6_2_Qgw.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_70_2_Lg9.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_71_1_Xk8.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_72_1_B8w.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_73_1_mLM.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_74_1_gln.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_75_1_DDJ.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_76_1_kGY.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_77_1_Pxs.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_78_1_UkX.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_79_1_ii4.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_7_2_1Zb.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_80_1_Bzq.root ',
	#'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_81_1_aUr.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_82_1_KL9.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_83_1_VAq.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_84_1_jyc.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_85_1_ReM.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_86_1_8Iq.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_87_1_ZIQ.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_88_1_UU0.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_89_1_ww6.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_8_2_L00.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_90_1_U76.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_91_1_f51.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_92_1_3uj.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_93_1_N5d.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_94_1_a9L.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_95_1_uNi.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_96_1_3Rm.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_97_1_bto.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_98_1_NTQ.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_99_1_AcO.root ',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2_10Par/cf41687776a1fcc13b844e2077c7e75b/out_reco_9_1_XM0.root ',

    )
)

process.TFileService = cms.Service("TFileService", fileName = cms.string("histo_10par_1000GeV.root") )

process.demoWithGEMs = cms.EDAnalyzer('GEMRecHitsReader',
	simHit = cms.untracked.InputTag("g4SimHits", "MuonGEMHits"),
	recHit = cms.untracked.InputTag("gemRecHits"),
	simTrack = cms.untracked.InputTag("mix", "MergedTrackTruth"),
	staTrack = cms.untracked.InputTag("standAloneMuons","UpdatedAtVtx","RECO"),
)

process.p = cms.Path(process.demoWithGEMs)
