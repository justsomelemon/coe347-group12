#!usr/bin/python3
import re
from matplotlib import pyplot as plt
import numpy as np
import os
import jpcm

from utils import *

sep = '/'
dr = 'postProcessing/sample/'
def contents(path): return [(f.name, path+f.name)
                            for f in os.scandir(path)]


def items(path): return [f.name for f in os.scandir(path)]
def path0(run): return datapath + run + sep + dr
def paths(run): return contents(path0(run))


def plotS(run, folder, name, path, ax=1, axV=0):
    # assumes sampling along Y unless otherwise specified (ax=1)
    # vector component is default selected as x-component (axV=0)
    axl = ['X', 'Y', 'Z']

    def title(tp): return (
        "Velocity {}-Component".format(axl[axV]) if tp == 1 else "Pressure Trace") + " vs " + axl[ax]
    namesave = name + "_" + axl[axV] + " vs " + axl[ax]
    print(name, path)
    data = np.loadtxt(path)
    if data.shape[1] > 4:
        tp = 1
        select = 3 + axV
        ylabel = "Velocity {}-Component".format(axl[axV])
    else:
        tp = 0
        select = 3
        ylabel = "π pressure [N/A]"

    print(title(tp))
    indep = data[:, ax]
    indep = (indep - min(indep)) / (max(indep) - min(indep))
    plt.plot(indep, data[:, select], c=jpcm.maps.ginshu)
    plt.title(title(tp))
    plt.xlabel(axl[ax] + '/L' + axl[ax] + ' [N/A]')
    plt.ylabel(ylabel)
    plt.savefig(plotpath2(run, folder, namesave), transparent=True)
    plt.close()


allruns = [f.name for f in os.scandir(datapath)]
runs = [run for run in allruns if not re.search('[a-zA-Z]', run)]
for run in runs:
    print("Plotting Samples for Run {}".format(run))
    for loc in paths(run):
        folder, path = loc
        for item in items(path):
            if "U" in item:
                plotS(run, folder, item, path+sep+item, axV=0)
                plotS(run, folder, item, path+sep+item, axV=1)
            else:
                plotS(run, folder, item, path+sep+item)
