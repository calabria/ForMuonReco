import FWCore.ParameterSet.Config as cms

#process = cms.Process("RecoSTAMuon")
process = cms.Process("AnalyzerSTA")
process.load("RecoMuon.Configuration.RecoMuon_cff")

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

	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_100_1_ex0.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_10_1_IhT.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_11_1_bvP.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_12_1_2Pq.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_13_1_t84.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_14_1_gyL.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_15_1_5iA.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_16_1_pLy.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_17_1_6Zs.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_18_1_ij1.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_19_1_HM3.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_1_1_t5y.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_20_1_Qzo.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_21_1_ocF.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_22_1_HJt.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_23_1_zaN.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_24_1_R0p.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_25_1_soo.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_26_1_xMF.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_27_1_NRR.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_28_1_hUV.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_29_1_hIn.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_2_1_Lal.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_30_1_z37.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_31_1_zcA.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_32_1_MIj.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_33_1_ufp.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_34_1_rIl.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_35_1_2gi.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_36_1_mg0.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_37_1_HiV.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_38_1_kCf.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_39_1_Jn6.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_3_1_bRu.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_40_1_yPE.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_41_1_4LC.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_42_1_hBm.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_43_1_yjm.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_44_1_41s.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_45_1_AUO.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_46_1_Jss.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_47_1_L0R.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_48_1_coB.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_49_1_wUI.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_4_1_wj1.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_50_1_4VX.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_51_1_z0L.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_52_1_T1g.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_53_1_bfN.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_54_1_ULA.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_55_1_Qg3.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_56_1_2tX.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_57_1_SCK.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_58_1_eSz.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_59_1_v1z.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_5_1_0hh.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_60_1_bR9.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_61_1_sUD.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_62_1_FUD.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_63_1_fnK.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_64_1_MFg.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_65_1_j7n.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_66_1_43H.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_67_1_E8h.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_68_1_D6I.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_69_1_PrB.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_6_1_7kG.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_70_1_Gsb.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_71_1_lfy.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_72_1_3wp.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_73_1_3fn.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_74_1_nNC.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_75_1_E0S.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_76_1_NOZ.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_77_1_kol.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_78_1_tVT.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_79_1_JNt.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_7_1_lnp.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_80_1_rHM.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_81_1_vbV.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_82_1_QUj.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_83_1_41a.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_84_1_FJL.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_85_1_kLZ.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_86_1_AYO.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_87_1_Z61.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_88_1_DDD.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_89_1_8xS.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_8_1_uti.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_90_1_kxO.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_91_1_YLh.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_92_1_5uT.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_93_1_CCu.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_94_1_JKm.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_95_1_TaB.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_96_1_osC.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_97_1_fFG.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_98_1_fBQ.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_99_1_vY0.root',
	'file:/lustre/cms/store/user/calabria/calabria_SingleMuPt40_GEN-SIM_CMSSW_6_1_2_SLHC6_patch1/calabria_SingleMuPt5_1000_RECO-GEM_RecHits_CMSSW_6_1_2_SLHC6_patch1/42a9166cac48036c69e0af3a481cbff4/step_GEM_LocalReco_9_1_pGF.root',

    )
)

#process.out = cms.OutputModule("PoolOutputModule",
#    fileName = cms.untracked.string('RecoSTAMuons.root')
#)

## Analyzer to produce pT and 1/pT resolution plots
process.STAMuonAnalyzer = cms.EDAnalyzer("STAMuonAnalyzer",
	DataType = cms.untracked.string('SimData'),
	StandAloneTrackCollectionLabel = cms.untracked.InputTag('standAloneMuons','','RECO'),
	MuonSeedCollectionLabel = cms.untracked.string('standAloneMuonSeeds'),
	rootFileName = cms.untracked.string('STAMuonAnalyzer_new.root'),
	NoGEMCase = cms.untracked.bool(True)
 	)

process.STAMuonAnalyzerWithGEMs = cms.EDAnalyzer("STAMuonAnalyzer",
	DataType = cms.untracked.string('SimData'),
	StandAloneTrackCollectionLabel = cms.untracked.InputTag('standAloneMuons','','RecoSTAMuon'),
	MuonSeedCollectionLabel = cms.untracked.string('standAloneMuonSeeds'),
	rootFileName = cms.untracked.string('STAMuonAnalyzerWithGEMs_new.root'),
	NoGEMCase = cms.untracked.bool(False)
	)

process.demo = cms.EDAnalyzer('GEMRecHitsReader',
	simHit = cms.untracked.InputTag("g4SimHits", "MuonGEMHits"),
	recHit = cms.untracked.InputTag("gemRecHits"),
	simTrack = cms.untracked.InputTag("mix", "MergedTrackTruth"),
	staTrack = cms.untracked.InputTag("standAloneMuons","","RECO"),
)

process.demoWithGEMs = cms.EDAnalyzer('GEMRecHitsReader',
	simHit = cms.untracked.InputTag("g4SimHits", "MuonGEMHits"),
	recHit = cms.untracked.InputTag("gemRecHits"),
	simTrack = cms.untracked.InputTag("mix", "MergedTrackTruth"),
	staTrack = cms.untracked.InputTag("standAloneMuons","","RecoSTAMuon"),
)

process.recHitPlots = cms.EDAnalyzer('TestGEMRecHitAnalyzer',
	RootFileName = cms.untracked.string("GEMRecHitHistograms.root"),

)

process.TFileService = cms.Service("TFileService", fileName = cms.string("histo.root") )

#process.globalMuons.MuonCollectionLabel = cms.InputTag("standAloneMuons","UpdatedAtVtx","RecoSTAMuon")
if includeGEMs:
	#process.p = cms.Path(process.standAloneMuons * process.STAMuonAnalyzerWithGEMs * process.STAMuonAnalyzer * process.recHitPlots)
	process.p = cms.Path(process.STAMuonAnalyzerWithGEMs * process.STAMuonAnalyzer * process.demoWithGEMs)
else:
	process.p = cms.Path(process.STAMuonAnalyzer * process.demo)

#process.this_is_the_end = cms.EndPath(process.out)

#Automatic addition of the customisation function from SLHCUpgradeSimulations.Configuration.combinedCustoms
#from SLHCUpgradeSimulations.Configuration.combinedCustoms import cust_2019

#call to customisation function cust_2019 imported from SLHCUpgradeSimulations.Configuration.combinedCustoms
#process = cust_2019(process)

# End of customisation functions 
