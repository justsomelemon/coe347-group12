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
                echo "-\ Copying Files..."
                cp -r "$run"* ../sim
                echo "-\ CD"
                cd ../sim/
                echo "-\ Staging"
                # python ../analysis/sample.py
                echo "-\ Allclean"
                ./Allclean
                echo "-\ Allrun"
                { time ./AllrunParallel 2>> time.txt ; } 
                echo "-\ Simulation Complete."
                echo "-\ Post-processing via Sample..."
                # postProcess -func sample -latestTime
                postProcess -func singleGraph -latestTime
                postProcess -func probes
                echo "-\ Complete."
                echo "-\ Copying Data..."
                rm -r processor*
                for step in $(ls -d *[0-9]*)
                do
                    mkdir -p ../data/"$run"
                    mv -f "$step"/ ../data/"$run"
                done
                mv constant/ ../data/"$run"
                mv postProcessing/ ../data/"$run"
                mv log.* ../data/"$run"
                echo "-\ Sweeping Dirt ..."
                # ./Allclean
                rm -r system/
                rm README.md
                # rm sets.txt
                echo "-\ CD"
                cd ../data/"$run"/
                echo "-\ Creating _.Foam ..."
                touch _.foam
                echo "-\ CD"
                cd ../../param/
                echo "-/| DONE |"
            fi
    esac
done
echo "-\| TIMING Data |"
mkdir -p ../data/time/
mv ../sim/time.txt ../data/time/
echo "  | UNINITIALIZE |"
for run in $(echo */)
do
    case "$run" in
        $runnames)
            rm -r "$run"
    esac
done
echo "  | CD |"
cd ../
echo "-/| DONE RUNNING---------------=||= - - -\\\\"    