import numpy as np
import jpcm
import matplotlib.pyplot as plt
from tqdm import tqdm
import itertools as it
#

# Time History Plotting
# just run and it will do everything


def data(run, type):

    varlen = 7 if type == 'U' else 3

    filepath = f"../data/{run}/postProcessing/probes/0/{type}"
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


def plotloc(name): return f"../../plots/{name}/"


def plot(name, type):
    da = data(name, type)
    opt = ""
    if da.shape[1] == 3:
        plt.plot(da[:, 0], da[:, 1], c=jpcm.maps.rurikon)
        plt.plot(da[:, 0], da[:, 2], c=jpcm.maps.enji_iro)
        plt.legend(["P at (x,y) = (5.5,0.5)", "P at (x,y) = (5.5,-0.5)"])
        plt.ylabel("Pressure (non-dimensional)")
        opt = "_P"
    else:
        leg = []
        pos = [" at (x,y) = (5.5,0.5)", " at (x,y) = (5.5,-0.5)"]
        cs = [jpcm.maps.rurikon, jpcm.maps.enji_iro]
        for i in range(2):
            plt.plot(da[:, 0], da[:, 1+3*i], c=cs[i], linestyle='solid')
            plt.plot(da[:, 0], da[:, 2+3*i], c=cs[i], linestyle='dashed')
            leg.extend([f"UX {pos[i]}", f"UY {pos[i]}"])
        plt.legend(leg)
        plt.ylabel("Velocity (non-dimensional)")
        opt = "_U"
    plt.xlabel("Time (non-dimensional)")
    plt.savefig(f"{plotloc(name)}Time{opt}.jpg")
    plt.close()


names = ["run_110_1", "run_110_2"]
types = ["U", "p"]
for n, t in it.product(names, types):
    plot(n, t)
