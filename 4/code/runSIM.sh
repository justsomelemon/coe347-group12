#!/bin/sh
# cd ${0%/*} || exit 1    # Run from this directory

# sh script to run every version of the simulation.

# 1) copy parameters from param/{i}/ to sim/
# 2) run simulation
# 3) move output to data/{i}/
# 4) delete parameter files from simulation directory

runnames=*run_* # all appropriate runs start with `run_`!
echo "-\| STAGING : "
echo "-\| INITIALIZE"
python3 analysis/param.py
cd sim/
touch time.txt
cd ../
cd param/
for run in $(echo */)
do
    case "$run" in
        $runnames)
            echo "Data Exists?..."
            if [[ -d "../data/$run" ]]
            then
                echo "Data Exists. Skipping Run $run."
            else
                if [[ -f "../work/$run/lock.icf" ]]
                then
                    echo "Data currently simulating. Skipping Run $run."
                else
                    echo "-\ Copying Files..."
                    mkdir -p ../work/"$run"
                    cp -r "$run"* ../work/"$run"
                    cp -r ../sim/* ../work/"$run"
                    echo "-\ CD"
                    cd ../work/"$run"
		            touch lock.icf
                    echo $PWD
                    echo "-\ Staging"
                    # python ../analysis/sample.py
                    echo "-\ Allclean"
                    ./Allclean
                    echo "-\ Allrun"
                    { time ./SIMrunParallel 2>> time.txt ; }
                    echo "-\ Simulation Complete."
		            rm lock.icf
		            exit 0
                fi
            fi
    esac
done
echo "  | CD |"
cd ../
echo "-/| DONE RUNNING---------------=||= - - -\\\\"
