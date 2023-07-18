#!/bin/bash -l
#bash start.sh list.csv

nsamples=$(wc -l < ${1})
((nsamples--))

echo "prepare result folder"
mkdir -p ./result

echo "The number of samples is ${nsamples}"
qsub -t 1-${nsamples} circRIPbatch.qsub ${1}