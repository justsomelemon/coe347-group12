#!/bin/bash

# See https://portal.tacc.utexas.edu/user-guides/stampede2/#running 
# for more details

#SBATCH -J of     # Job name
#SBATCH -o ofo.%j       # Name of stdout output file
#SBATCH -e ofe.%j       # Name of stderr error file

### #SBATCH -p normal          # Queue (partition) name
#SBATCH -p development          # Queue (partition) name
### #SBATCH -p skx-normal          # Queue (partition) name

#SBATCH -N 1               # Total # of nodes
#SBATCH -n 68               # Total # of mpi tasks
#SBATCH -t 01:00:00        # Run time (hh:mm:ss)

#SBATCH --mail-user=akhil.sadam@utexas.edu
#SBATCH --mail-type=all    # Send email at begin and end of job

#SBATCH -A COE-347-S22       # Allocation name (req'd if you have more than 1)

# Other commands must follow all #SBATCH directives...
### # note the following 'openfoam/' directory is the same as your 'remote' directory
cdw
cd openfoam/code/

pwd
date

sh runTACC.sh

date