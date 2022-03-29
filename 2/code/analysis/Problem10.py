import numpy as np
import jpcm
import matplotlib.pyplot as plt
from tqdm import tqdm
import itertools as it
#


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

# generate F' in units of \rho U^2 L


run = 'run_20_2'
bp = data(
    run, 'p', filepath=f"../data/{run}/postProcessing/forcelines/9.6/back_p.xy")
fp = data(
    run, 'p', filepath=f"../data/{run}/postProcessing/forcelines/9.6/front_p.xy")
bu = data(
    run, 'U', filepath=f"../data/{run}/postProcessing/forcelines/9.6/back_U.xy")
fu = data(
    run, 'U', filepath=f"../data/{run}/postProcessing/forcelines/9.6/front_U.xy")


def dy(da):
    xs = da[:, 1]
    dy = (- xs[1:] + xs[:-1]).tolist()
    dy.append(dy[-1])  # last element impute
    return np.array(dy)


def intr(dx, v):
    return np.dot(dx, v)


def p(da):
    return da[:, 3]


def UXT(da):
    ux = da[:, 3]
    uy = da[:, 4]
    uz = da[:, 5]
    u = np.sqrt(ux**2 + uy**2 + uz**2)
    return u*ux


dfp = intr(dy(fp), p(fp)) - intr(dy(bp), p(bp))
dfu = intr(dy(fu), UXT(fu)) - intr(dy(bu), UXT(bu))
force = dfp + dfu
print(f"Non-dimensionalized Force: {force}")
print(f"Cd: {2*force}")
