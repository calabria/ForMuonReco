import FWCore.ParameterSet.Config as cms

process = cms.Process("AnalyzerGLB2")
#process.load("RecoMuon.Configuration.RecoMuon_cff")

process.options = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )

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
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, 'auto:upgrade2019', '')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(

	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_100_1_Zsj.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_10_1_fnW.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_11_1_Vga.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_1_1_sR2.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_12_1_BuW.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_13_1_7CE.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_14_1_mU8.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_15_1_eGY.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_16_1_XgR.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_17_1_pDh.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_18_1_Hks.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_19_1_Y5g.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_20_1_o3W.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_21_1_fwb.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_2_1_feM.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_22_1_HvP.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_23_1_Ihm.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_24_1_Pun.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_25_1_0eY.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_26_1_7O5.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_27_1_jgA.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_28_1_YXU.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_29_1_vio.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_30_1_XGK.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_31_1_kRB.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_3_1_uE1.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_32_1_hui.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_33_1_UWj.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_34_1_U7m.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_35_1_EAO.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_36_1_Gp4.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_37_1_Dwc.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_38_1_pT3.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_39_1_xM0.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_40_1_xMj.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_41_1_p6l.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_4_1_qcb.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_42_1_RDV.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_43_1_1xd.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_44_1_ydU.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_45_1_FX5.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_46_1_ZdQ.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_47_1_SLj.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_48_1_WM4.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_49_1_saN.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_50_1_x8o.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_51_1_kvO.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_5_1_Ko4.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_52_1_hnh.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_53_1_rff.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_54_1_ffJ.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_55_1_kkG.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_56_1_enk.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_57_1_48w.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_58_1_Q6j.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_59_1_wCS.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_60_1_bGf.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_61_1_Mzs.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_6_1_M1w.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_62_1_l7K.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_63_1_t0m.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_64_1_6K9.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_65_1_VHh.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_66_1_mwI.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_67_1_JEc.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_68_1_1e8.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_69_1_z6j.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_70_1_8kX.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_71_1_iYj.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_7_1_sT6.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_72_1_5TQ.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_73_1_XOe.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_74_1_xnK.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_75_1_ieb.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_76_1_TmW.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_77_1_xQV.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_78_1_iqd.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_79_1_BFn.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_80_1_Ym8.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_81_1_bmo.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_8_1_oRS.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_82_1_Rqh.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_83_1_6rh.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_84_1_hzE.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_85_1_AXU.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_86_1_Sro.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_87_1_ZcB.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_88_1_sP8.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_89_1_sPy.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_90_1_Rii.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_91_1_eM4.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_9_1_eBD.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_92_1_LGB.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_93_1_2Bd.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_94_1_mmE.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_95_1_NVD.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_96_1_9Bk.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_97_1_hqe.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_98_1_YGv.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt1000_GEN-SIM-DIGI-RECO_CMSSW_6_2_0_SLHC1_v2/calabria_SingleMuPt1000_StdRECO_62X_SLHC/9d4158c7f7160e8742c9656b5dc7afdf/out_reco_std_99_1_Ezl.root',

    )
)

process.TFileService = cms.Service("TFileService", fileName = cms.string("histo.root") )

process.out = cms.OutputModule("PoolOutputModule",
    	fileName = cms.untracked.string('/lustre/cms/store/user/calabria/RecoGLBMuons_62X.root'),
	SelectEvents = cms.untracked.PSet(
		SelectEvents = cms.vstring('p')
	)
)

process.selecteGLB = cms.EDFilter('SelectMuonByChargeAss',
	StandAloneTrackCollectionLabel = cms.untracked.InputTag('globalMuons','','AnalyzerGLB'),
	StandAloneGemTrackCollectionLabel = cms.untracked.InputTag('globalMuons','','RECO'),
	filter = cms.bool(True)
)

#process.globalMuons.MuonCollectionLabel = cms.InputTag("standAloneMuons","UpdatedAtVtx","")
process.p = cms.Path(process.selecteGLB)

#Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.combinedCustoms
from SLHCUpgradeSimulations.Configuration.combinedCustoms import cust_2019

#call to customisation function cust_2019 imported from SLHCUpgradeSimulations.Configuration.combinedCustoms
process = cust_2019(process)

# End of customisation functions

process.outpath = cms.EndPath(process.out)
