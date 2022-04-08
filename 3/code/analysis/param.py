import itertools
import json as js
import os
import numpy as np
import cylwall as cyw
import blockMeshDict as bmd

# set up default parameters for each run.
# assuming U, L = 1.
U = 1
L = 1

TDREH = 40  # Time-Dependency Reynolds Threshold
LFRETH = 60  # Laminar-Flow Reynolds Threshold

pathNames = ["constant/thermophysicalProperties", "system/controlDict",
             "system/decomposeParDict", "system/singleGraph"]
bmdpath = "system/blockMeshDict"
pinames = []
keynames = ['f', 'cores']

parampath = "param/"

setpath = f"{parampath}settings.json"
templatepath = f"{parampath}template/"
def newpath(i): return f"{parampath}{i}/"
def items(path): return [f.name for f in os.scandir(path)]


def generateParameters(settings):
    # pi defaults
    class pi:
        Re = 10

    # pis

    for name in pinames:
        if name in settings.keys():
            setattr(pi, name, settings[name])

    # key defaults

    class key:

        f = 8

        # not using a core to leave some headroom.
        if len(os.sched_getaffinity(0)) > 16:
            # this is TACC
            coreMax = 64
            cores = 64  # maximum is 64 for knl, atleast atm
        else:
            coreMax = min(len(os.sched_getaffinity(0)), 64)
            cores = coreMax-1

        dt = 0.02/f

        # Same here : NEEDS TO BE INT
        # these ar for feeding into the string in blockMeshDict_utils.py
        AAA = np.array([3*f, 1*f, 1]).astype(str)
        BBB = np.array([3*f, 4*f, 1]).astype(str)
        CCC = np.array([12*f, 4*f, 1]).astype(str)

    # keys

    for name in keynames:
        if name in settings.keys():
            setattr(key, name, settings[name])

    if key.cores > key.coreMax:
        key.cores = key.coreMax

    def updateKey(f):

        key.dt = 0.02/f

        # Same here : NEEDS TO BE INT
        # these ar for feeding into the string in blockMeshDict_utils.py
        key.AAA = np.array([3*f, 1*f, 1]).astype(str)
        key.BBB = np.array([3*f, 4*f, 1]).astype(str)
        key.CCC = np.array([12*f, 4*f, 1]).astype(str)
    updateKey(key.f)

    # param defaults

    def dp(n, left):  # returns tuple (cost, [factors])
        memo = {}
        if left == 1:
            return (n, [n])

        i = 2
        best = n
        bestTuple = [n]
        while i ** 2 <= n:
            if n % i == 0:
                rem = dp(n / i, left - 1)
                if rem[0] + i < best:
                    best = rem[0] + i
                    bestTuple = [i] + rem[1]
            i += 1

        memo[(n, left)] = (best, bestTuple)
        return memo[(n, left)]

    def splitF(n):
        left = 2
        _, factors = dp(n, left)
        print(factors)
        while len(factors) < left:
            factors.append(1)
        return f"{int(factors[0])} {int(factors[1])}"

    params = \
        [

            {
            },

            {
                'deltaT': key.dt,
            },


            {  # should not be changed if possible
                'numberOfSubdomains': key.cores,
                'n': splitF(key.cores)
            },

            {
                'A':
                f"""\n\tstart   (0 0.00001 0);\n\tend     (0.6 0.00001 0);
                    """,
                'B':
                f"""\n\tstart   (0.59999 0.00001 0);\n\tend     (0.59999 0.20001 0);
                    """,
                'C':
                f"""\n\tstart   (0.59999 0.20001 0);\n\tend     (3 0.20001 0);
                    """,
                'D':
                f"""\n\tstart   (0 0.99999 0);\n\tend     (3 0.99999 0);
                    """
            }

        ]

    # and params

    for param in params:
        for keyc in param.keys():
            if keyc in settings.keys():
                param[keyc] = settings[keyc]

    return params, key


def cpy(SRC_DIR, TARG_DIR):
    os.system(f"cp -Rvn {SRC_DIR} {TARG_DIR}")


def _replace(txt: str, params, replaceval='XXX'):
    lines = txt.split('\n')
    for p in params:
        for i in range(len(lines)):
            line = lines[i]
            if p in line:
                lines[i] = line.replace(replaceval, str(params[p]))
    return '\n'.join(lines)
    # for p in params:
    #     txt = txt.replace(replaceval, p.value)
    # return txt


def replace(path, item, parameters):
    with open(path+item, 'r') as file:
        txt = file.read()
    txt = _replace(txt, parameters)
    with open(path+item, 'w') as file:
        file.write(txt)


with open(setpath, 'r') as file:
    sets = js.load(file)

for set in sets:
    parameters, key = generateParameters(set)
    print(parameters)
    path = newpath(set['id'])
    os.makedirs(path, exist_ok=True)
    cpy(f'{templatepath}*', path)
    for i in range(len(pathNames)):
        replace(path, pathNames[i], parameters[i])
    bmd.generate(path+bmdpath, key)
