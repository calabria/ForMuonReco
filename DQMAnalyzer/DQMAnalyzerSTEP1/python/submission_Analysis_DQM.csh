#!/bin/bash

path=$CMSSW_BASE/src/DQMAnalyzer/DQMAnalyzerSTEP1/python/CFGFiles/DQM

for i in `cat ListDirectories.txt`; do

	cd $path/$i
	for batch in `ls $path/$i/*.csh`; do

        	chmod 775 ${batch}
        	qsub -q local ${batch}
        	echo $batch "submitted"

	done

done

