#!bin/sh

# sh script to run every version of the simulation.

# 1) copy parameters from param/{i}/ to sim/
# 2) run simulation
# 3) move output to data/{i}/ 
# 4) delete parameter files from simulation directory

echo "-\| INITIALIZE"
cd param/
for run in $(echo */)
do
    echo "-\ Copying Files..."
    cp -r "$run"* ../sim
    echo "-\ CD"
    cd ../sim/
    echo "-\ Staging"
    python ../analysis/sample.py
    echo "-\ Allclean"
    ./Allclean
    echo "-\ Allrun"
    time ./Allrun
    echo "-\ Simulation Complete."
    echo "-\ Post-processing via Sample..."
    postProcess -func sample
    echo "-\ Complete."
    echo "-\ Copying Data..."
    for step in $(ls -d *[0-9]*)
    do
        mkdir -p ../data/"$run"
        mv -f "$step"/ ../data/"$run"
    done
    mv -f constant/ ../data/"$run"
    mv -f postProcessing/ ../data/"$run"
    echo "-\ Sweeping Dirt ..."
    # ./Allclean
    rm -r system/
    rm README.txt
    rm sets.txt
    echo "-\ CD"
    cd ../data/"$run"/
    echo "-\ Creating _.Foam ..."
    touch _.foam
    echo "-\ CD"
    cd ../../param/
    echo "-/| DONE"
done
    