#!/bin/bash

# See https://portal.tacc.utexas.edu/user-guides/stampede2/#running 
# for more details

#SBATCH -J of     # Job name
#SBATCH -o ofo.%j       # Name of stdout output file
#SBATCH -e ofe.%j       # Name of stderr error file

### #SBATCH -p normal          # Queue (partition) name
### #SBATCH -p development          # Queue (partition) name
#SBATCH -p skx-normal          # Queue (partition) name

#SBATCH -N 1               # Total # of nodes
#SBATCH -n 48               # Total # of mpi tasks
#SBATCH -t 04:00:00        # Run time (hh:mm:ss)

#SBATCH --mail-user=akhil.sadam@utexas.edu
#SBATCH --mail-type=all    # Send email at begin and end of job

#SBATCH -A COE-347-S22       # Allocation name (req'd if you have more than 1)

# Other commands must follow all #SBATCH directives...

pwd
date

echo "[+] RUN : MODULE LOAD." 
module purge
module load intel/18.0.2  libfabric/1.7.0  impi/18.0.2 
module load python3
module load openfoam/7.0
module list
echo "[+] RUN : SLURM RUN." 
sh runTACC.sh &
process_id=$!
echo "[+] RUN : SLURM RUN - PID: $process_id"
wait $process_id
echo "[+] RUN : SLURM RUN - Exit status: $?"
echo "[+] ANALYZE : MODULE LOAD" 
module load gcc/9.1.0
module load swr/21.2.5
module load qt5/5.14.2
module load oneapi_rk/2021.4.0
module load paraview/5.10.0
echo "[+] ANALYZE : PIP3 INSTALL" 
pip3 install --user jpcm colour-science pynverse scandir
echo "[+] ANALYZE : SCRIPT" 
sh analyze.sh

date