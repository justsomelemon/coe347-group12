export OMP_NUM_THREADS=192
module purge
module load intel/18.0.2  libfabric/1.7.0  impi/18.0.2 
module load python3
module load openfoam/7.0
module list
. $WM_PROJECT_DIR/bin/tools/RunFunctions
sh parReconstructPar -n 40