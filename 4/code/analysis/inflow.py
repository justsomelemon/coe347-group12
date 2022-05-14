import numpy as np
import jpcm
import os
import matplotlib.pyplot as plt
from tqdm import tqdm

# run from code folder

length = 0.5


def inflow(p):
    pt = f'{p}/postProcessing/singleGraph/'
    xs = []
    ys = []
    ys2 = []
    for d in os.listdir(pt):
        q = (pt+d)
        xs.append(float(d))
        dat = np.genfromtxt(f'{q}/D_U.xy')
        raw = dat[:, 4]
        infl = raw[raw < 0]
        ys.append(-length*np.mean(raw))
        ys2.append(-length*(len(infl) / len(raw))*np.mean(infl))
    x = sorted(xs)
    y1 = [ysi for _, ysi in sorted(zip(xs, ys), key=lambda pair: pair[0])]
    y2 = [ysi for _, ysi in sorted(zip(xs, ys2), key=lambda pair: pair[0])]
    return np.array(x), np.array(y1), np.array(y2)


path = "data/"
plpath = '../plots/'

for dir in os.listdir(path):
    if 'run' in dir:
        p = path+dir
        _, mf, re, win, wall = dir.split('_')[:5]
        x, y, y2 = inflow(p)
        plt.plot(x, y, c=jpcm.maps.kokushoku)
        plt.plot(x, y2, c=jpcm.maps.rurikon)
        plt.plot(x, y2-y, c=jpcm.maps.karakurenai)
        plt.legend(['Net Inflow', 'Inflow', 'Outflow'])
        plt.title(
            f'Inflow over Time along slice D\n(Re {re}, Window {win}, Wall {wall} at MeshFactor {mf})')
        plt.xlabel('Time [nondimensionalized (ndl)]')
        plt.ylabel('Inflow [ndl in U*L units]')
        plt.savefig(f'{plpath}/{dir}/inflow.png')
        plt.close()
