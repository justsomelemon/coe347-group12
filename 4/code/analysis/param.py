import itertools
import json as js
import os
import numpy as np
import cylwall as cyw
import blockMeshDict as bmd

# set up default parameters for each run.
# assuming U, L = 1.
U = 1.0
L = 1.0

TDREH = 40  # Time-Dependency Reynolds Threshold
LFRETH = 60  # Laminar-Flow Reynolds Threshold

pathNames = ["constant/transportProperties",
             "system/controlDict", "system/decomposeParDict", "system/singleGraph", "system/probes"]
bmdpath = "system/blockMeshDict"
pinames = ['Re']
keynames = ['f', 'e', 'w', 'H', 'a', 'b', 'cores']

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
        # NEEDS TO BE INT, mesh size would be nice to be inversely dependent on Re for laminar flow (sufficient but unnecessary condition),
        # but that is not at all possible unless TACC simulates one plot for a week!
        f = int(max(10, pi.Re/3))  # int(min(pi.Re, LFRETH))

        L = L
        H = L
        e = 0.05
        w = 0.1

        a = 0.05

        # not using a core to leave some headroom.
        if len(os.sched_getaffinity(0)) > 16:
            # this is TACC
            coreMax = 8
            cores = 8  # forcing 2-process on TACC
        else:
            coreMax = min(len(os.sched_getaffinity(0)), 192)
            cores = coreMax - 1

    # keys

    for name in keynames:
        if name in settings.keys():
            setattr(key, name, settings[name])

    if key.cores > key.coreMax:
        key.cores = key.coreMax

    def updateKey(f):

        key.dt = 0.008/f
        key.T0 = (key.L)/U
        key.et = 60*key.T0
        key.wt = 0.1

        try:
            x = key.b
        except Exception:
            key.b = (key.L)/2

        key.m = key.b - 0.5*key.a
        key.n = key.b + 0.5*key.a
        print(key.m)
        print(key.n)
        key.p = key.H + key.w
        key.q = key.H + key.w + 2*key.e
        key.r = key.L - key.n

        pczn = 100000
        key.m = int(key.m * pczn)/pczn
        key.n = int(key.n * pczn)/pczn
        key.p = int(key.p * pczn)/pczn
        key.q = int(key.q * pczn)/pczn
        key.r = int(key.r * pczn)/pczn
        key.e = int(key.e * pczn)/pczn
        key.a = int(key.a * pczn)/pczn
        key.w = int(key.w * pczn)/pczn

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

    eps = 0.0001
    params = \
        [
            {
                'nu': 1/pi.Re,
            },

            {
                'endTime': key.et,
                'writeControl': 'runTime',
                'writeInterval': key.wt,
                'deltaT': key.dt,
            },

            {  # should not be changed if possible
                'numberOfSubdomains': key.cores,
                'n': splitF(key.cores)
            },

            {
                'A':
                f"""\n\tstart   ({(key.m+eps):.6f} {(key.p-eps):.6f} 0);\n\tend     ({(key.n-eps):.6f} {(key.p-eps):.6f} 0);
                    """,
                'B':
                f"""\n\tstart   ({(key.m+eps):.6f} {(key.p-eps):.6f} 0);\n\tend     ({(key.m+eps):.6f} {(key.H+eps):.6f} 0);
                    """,
                'C':
                f"""\n\tstart   ({(key.n-eps):.6f} {(key.p-eps):.6f} 0);\n\tend     ({(key.n-eps):.6f} {(key.H+eps):.6f} 0);
                    """,
                'D':
                f"""\n\tstart   ({(key.m+eps):.6f} {(key.H+eps):.6f} 0);\n\tend     ({(key.n-eps):.6f} {(key.H+eps):.6f} 0);
                    """,
                'E':
                f"""\n\tstart   ({(key.b+eps):.6f} {(key.H+eps):.6f} 0);\n\tend     ({(key.b+eps):.6f} 0 0);
                    """,
            },

            {
                'probeLocations': f'\n    ({(key.n-eps-0.025):.6f} 0.95 0)\n    ({(key.n-eps+0.025):.6f} 0.95 0)',
            },
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
    for p, i in itertools.product(params, range(len(lines))):
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
