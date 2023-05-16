# circRIP_container
Singularity container for circRIP


# 0. build the container
## 0.1 To build the container
Assume you are using computational cluster without root privilege.

For BU SCC user
    If you are using BU SCC, please switch to SCC-i01 using the command below
```bash
ssh SCC-i01
cd /path/to/folder
```

Build the container using fakeroot mode
```bash
git clone git@github.com:90yearsoldcoder/circRIP_container.git
cd circRIP_container
singularity build --fakeroot circRIP.sif circRIP.def
```

## 0.2 Run container in SHELL mode(for developer)
It is used for debugging and debuging only. You can get into the container and check the environment in this way.
```bash
singularity shell --no-home --bind ./inputdata:/inputdata,./result:/result,/restricted/projectnb/casa/mtLin/reference:/reference circRIP.sif
```

And activate the conda environment
```
source activate circRIP
```

Command line for test
```
python circRIP.py EnrichedcircRNA -ip_circ inputdata/WB_LJ_PS_EX2_49_S49_L001.circ -input_circ inputdata/WB_LJ_PS_EX2_33_S33_L001.circ -gtf /reference/gencode.v40.annotation.gtf \
                  -ip_bam inputdata/WB_LJ_PS_EX2_49_S49_L001.bam -input_bam inputdata/WB_LJ_PS_EX2_33_S33_L001.bam -prefix test.final.out \
		          -G /reference/GRCh38.primary_assembly.genome.fa
```

# 1. perform circlexplore3
follow the circlexplore3 singularity instruct to generate the result
```
https://github.com/90yearsoldcoder/circlexplore3_pipeline.git
```

The result folder should contain four folders: 
``` circ ``` 
``` fusion ```
``` hisat ```
``` quant ```

# 2. process the circlexplore3 result

## 2.1 Only For one single file(otherwise, go to 2.2)
Assume the result is at ``` path/to/result ```
Then run the circ3postprocess.py to copy the neccessary files and modify them
```bash
python circ3postprocess.py -n <sample_name>  -p path/to/result
```
The processed files will be in ``` current/path/inputdata ```

## 2.2 For a batch file
### 2.2.1 prepare a list file
The ```list.csv``` should be in current path(circRIP_container)
Format is below:

| Input_result_folder | Input_sample_name        | IP_result_folder | IP_sample_name         | Pair_name |
|---------------------|--------------------------|------------------|------------------------|-----------|
| input/result/       | WB_LJ_PS_EX2_33_S33_L001 | elute/result/    | WB_LJ_PS_EX2_49_S49_L001 | C1        |
| input/result/       | WB_LJ_PS_EX2_34_S34_L001 | elute/result/    | WB_LJ_PS_EX2_50_S50_L001 | C2        |
| input/result/       | WB_LJ_PS_EX2_35_S35_L001 | elute/result/    | WB_LJ_PS_EX2_51_S51_L001 | C3        |
| input/result/       | WB_LJ_PS_EX2_37_S37_L001 | elute/result/    | WB_LJ_PS_EX2_53_S53_L001 | C5        |
| input/result/       | WB_LJ_PS_EX2_38_S38_L001 | elute/result/    | WB_LJ_PS_EX2_54_S54_L001 | C6        |
| input/result/       | WB_LJ_PS_EX2_40_S40_L001 | elute/result/    | WB_LJ_PS_EX2_56_S56_L001 | C8        |
| input/result/       | WB_LJ_PS_EX2_43_S43_L001 | elute/result/    | WB_LJ_PS_EX2_59_S59_L001 | A3        |
| input/result/       | WB_LJ_PS_EX2_44_S44_L001 | elute/result/    | WB_LJ_PS_EX2_60_S60_L001 | A4        |
| input/result/       | WB_LJ_PS_EX2_45_S45_L001 | elute/result/    | WB_LJ_PS_EX2_61_S61_L001 | A5        |
| input/result/       | WB_LJ_PS_EX2_46_S46_L001 | elute/result/    | WB_LJ_PS_EX2_62_S62_L001 | A6        |
| input/result/       | WB_LJ_PS_EX2_47_S47_L001 | elute/result/    | WB_LJ_PS_EX2_63_S63_L001 | A7        |
| input/result/       | WB_LJ_PS_EX2_48_S48_L001 | elute/result/    | WB_LJ_PS_EX2_64_S64_L001 | A8        |

### 2.2.2 run the bash code
```
bash circ3postprocess.sh list.csv 
```
The processed files will be in ``` current/path/inputdata ```


