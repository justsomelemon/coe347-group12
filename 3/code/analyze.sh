#!bin/sh

# sh script to analyze every version of the simulation.

# 1) analyze data from data/{i}/
# 2) save output to ../plots/{i}/

cd analysis
echo "Analyzing Samples With PARAVIEW:"
pvpython default.py
echo "Analyzing Samples With MATPLOTLIB:"
python3 sampled.py
# python3 time.py
cd ..