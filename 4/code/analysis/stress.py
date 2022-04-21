#!usr/bin/python3
import re
from matplotlib import pyplot as plt
import numpy as np
import os
import jpcm
from ast import literal_eval as make_tuple

from utils import *

sep = '/'
dr = '0.5/'
def contents(path): return [(f.name, path)
                            for f in os.scandir(path)]


def items(path): return [f.name for f in os.scandir(path)]
def path0(run): return datapath + run + sep + dr
def paths(run): return contents(path0(run))


def calcstress(data, h):
    return (data[:, 0]-data[:, 1])/h


def plotS(run, folder, path):
    # assumes sampling along Y unless otherwise specified (ax=1)
    # vector component is default selected as x-component (axV=0)
    axl = ['X', 'Y', 'Z']

    print(path)
    with open(path, 'r') as filehandle:
        lines = filehandle.readlines()
        nline = int(lines[19])
        data = lines[21:21+nline]
        data = np.array([np.array(make_tuple(x.strip('\n').replace(' ', ',')))
                         for x in data])
    print(data.shape)

    side = int(np.sqrt(data.shape[0]))
    h = 0.1/side

    vx = data[:, 0]
    vx = vx.reshape(side, side, order='A')
    print(vx[::2, :])
    vx = np.concatenate((vx[0::2, :], vx[1::2, :]), axis=1)
    # vx[1::2, :] = vx[1::2, ::-1]
    stress = calcstress(data, h)
    # print(title(tp))
    # indep = data[:, ax]
    indep = np.array(list(range(len(stress))))
    indep = indep/max(indep)
    plt.plot(indep, stress, c=jpcm.maps.ginshu)
    plt.title("Stress on Lid")
    plt.xlabel('X/L')
    plt.ylabel('Stress')
    plt.savefig(plotpath2(run, folder, 'Stress'), transparent=True)
    plt.close()


allruns = [f.name for f in os.scandir(datapath)]
runs = [run for run in allruns if not re.search('[a-zA-Z]', run)]
for run in runs:
    print("Plotting Stress for Run {}".format(run))
    for loc in paths(run):
        folder, path = loc
        for item in items(path):
            if "U" in item:
                plotS(run, folder, path+sep+item)
        break
