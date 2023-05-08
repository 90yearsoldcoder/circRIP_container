# circRIP_container
Singularity container for circRIP


# build the container
## To build the container
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

## Run container in SHELL mode(for developer)
It is used for debugging and debuging only. You can get into the container and check the environment in this way.
```bash
singularity shell --no-home --bind ./inputdata:/inputdata,./result:/result,/restricted/projectnb/casa/mtLin/reference:/reference circRIP.sif
source activate circRIP
```

# perform circlexplore3
follow the circlexplore3 singularity instruct to generate the result
```
https://github.com/90yearsoldcoder/circlexplore3_pipeline.git
```

The result folder should contain four folders: 
``` circ ``` 
``` fusion ```
``` hisat ```
``` quant ```

# process the circlexplore3 result
Assume the result is at ``` path/to/result ```
Then run the circ3postprocess.py to copy the neccessary files and modify them
```bash
python circ3postprocess.py <sample_name>  path/to/result
```
The processed files are all in ``` current/path/inputdata ```
