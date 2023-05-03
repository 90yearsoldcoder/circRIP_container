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
singularity build --fakeroot cirRIP.sif circRIP.def
```