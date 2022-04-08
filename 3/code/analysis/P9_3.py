import numpy as np
import jpcm
import matplotlib.pyplot as plt
from tqdm import tqdm
import itertools as it


def data(run, type, filepath=None):

    if filepath is None:
        filepath = f"../data/{run}/postProcessing/probes/0/{type}"

    varlen = 6 if type == 'U' else 4

    with open(filepath, 'r') as file:
        text = file.read()
    text = text.replace("(", "").replace(")", "").replace(
        "             ", " ").replace("\t", "").split("\n")
    text = text[4:]
    data = np.zeros(shape=(len(text)-1, varlen))
    for i in tqdm(range(len(text)-1)):
        line = text[i].split(" ")
        linedata = [float(l) for l in line if len(l) > 0]
        data[i, :] = linedata
    return data


for i in range(4):
    run = f'run_20_{i+1}'
    rl = data(
        run, 'U', filepath=f"../data/{run}/postProcessing/singleGraph/9.6/recirculation_U.xy")
    indx = np.where(rl[:, 3] > 0)[0][0]
    pos = rl[indx, 0]
    print(f"RUN: {run} : length ={pos-0.5}")
