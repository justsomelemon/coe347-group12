# deploy, run, analyze and return data from TACC remote server

# input

# sh core.sh -p=<project #> -r="<specific tacc directory>" -u="<tacc username>" -i="<tacc_id_#>"

FOLDER=$PWD/../
PROJECT=4
REMOTE="openfoam/"
USERNAME="as_tacc"

for i in "$@"; do
  case $i in
    -f=*|--folder=*)
      FOLDER="${i#*=}"
      shift # past argument=value
      ;;
    -p=*|--project=*)
      PROJECT="${i#*=}"
      shift # past argument=value
      ;;
    -r=*|--remote=*)
      REMOTE="${i#*=}"
      shift # past argument=value
      ;;
    -u=*|--username=*)
      USERNAME="${i#*=}"
      shift # past argument=value
      ;;
    -t=*|--taccid=*)
      TACCID="${i#*=}"
      shift # past argument=value
      ;;
    --default)
      DEFAULT=YES
      shift # past argument with no value
      ;;
    -*|--*)
      echo "Unknown option $i"
      exit 1
      ;;
    *)
      ;;
  esac
done

echo "FOLDER = ${FOLDER}"
echo "PROJECT = ${PROJECT}"
echo "REMOTE = ${REMOTE}"
echo "USERNAME = ${USERNAME}"
echo ""
read -p "[?] Would you like to continue? Please verify the above information first."

# deploy

folder="${FOLDER}""${PROJECT}"/code
files="${folder}/runTACC.sh ${folder}/run.slurm ${folder}/analyze.sh ${folder}/param/ ${folder}/sim/ ${folder}/analysis/"
remote="${USERNAME}"@stampede2.tacc.utexas.edu

# echo "[-] INITALIZE : SSH Directories." 
# ssh -tt "${remote}" << EOF 
#  cdw
#  mkdir -p "${REMOTE}"code 
#  mkdir -p "${REMOTE}"code/analysis/
#  mkdir -p "${REMOTE}"code/data/
#  mkdir -p "${REMOTE}"code/param/
#  mkdir -p "${REMOTE}"code/sim/
#  mkdir -p "${REMOTE}"plots/
#  exit
# EOF

echo ""

echo "[-] INITALIZE : SCP files." 
scp -r ${files} "${remote}":\$WORK/"${REMOTE}"code/
echo ""
echo "[-] RUN : TACC." 
ssh -tt "${remote}" << EOF 
cdw
cd "${REMOTE}"code
cd sim/
chmod +x *
cd ../
sbatch run.slurm
EOF


# minor change to core.sh
# we want the below polling code to run, but I haven't fixed it yet, so please just wait to run that last command

# job_id=$(sbatch run.slurm)
# job_done=0
# while [ "$job_done" -neq "slurm_load_jobs error: Invalid job id specified" ]
# do
#     job_done=$(squeue ${job_id})
#     sleep 60
# done

echo ""

read -p "[?] Would you like to continue? Only do so once job has completed!"

echo "[-] COPYBACK : SCP files." 
scp -r "${remote}":\$WORK/"${REMOTE}"code/data/ "${folder}"/
scp -r "${remote}":\$WORK/"${REMOTE}"plots/ "${FOLDER}""${PROJECT}"/
echo ""
echo "[|] COMPLETE -\\\\\\\\-=||"

