#!/bin/bash

mkdir /lustre/cms/store/user/calabria/DQMGem/

cd $CMSSW_BASE/src/DQMAnalyzer/DQMAnalyzerSTEP1/python/

for i in `cat ListDirectories.txt`; do

	rm -r ./CFGFiles/DQM/$i
	mkdir ./CFGFiles/DQM/$i

done


cmsRun batchsubmission_DQM_cfg.py
