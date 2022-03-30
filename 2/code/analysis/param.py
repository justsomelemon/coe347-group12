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

pathNames = ["constant/transportProperties",
             "system/controlDict", "system/decomposeParDict", "system/probes", "system/singleGraph"]
bmdpath = "system/blockMeshDict"
pinames = ['Re']
keynames = ['f', 'R', 'R2', 'H', 'F', 'W', 'K', 'cores']

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
        # NEEDS TO BE INT, mesh size should be inversely dependent on Re for laminar flows,
        # but that is not at all possible unless TACC simulates one plot for a week!
        f = int(max(10, pi.Re/3))  # int(min(pi.Re, LFRETH))

        R = L/2
        R2 = 3*L/2
        H = 4
        F = 4
        W = 4 + pi.Re*(1/15)
        K = 4
        # not using a core to leave some headroom.
        if len(os.sched_getaffinity(0)) > 16:
            # this is TACC
            coreMax = 192
            cores = 192  # forcing octa-node on TACC
        else:
            coreMax = min(len(os.sched_getaffinity(0)), 192)
            cores = coreMax - 1

        dt = 0.02/f

        T0 = (F+W)/U

        if pi.Re > TDREH:
            et = 6*T0
            wt = 0.1
        else:
            et = T0+0.3
            wt = 0.1

        # Same here : NEEDS TO BE INT
        # these ar for feeding into the string in blockMeshDict_utils.py
        AAA = np.array([1*f, 2*f, 1]).astype(str)
        BBB = np.array([3*f, 2*f, 1]).astype(str)
        CCC = np.array([3*f, 3*f, 1]).astype(str)
        DDD = np.array([2*f, 3*f, 1]).astype(str)
        EEE = np.array([int(1.5*f), 3*f, 1]).astype(str)
        FFF = np.array([int(1.5*f), 2*f, 1]).astype(str)

    # keys

    for name in keynames:
        if name in settings.keys():
            setattr(key, name, settings[name])

    if key.cores > key.coreMax:
        key.cores = key.coreMax

    def updateKey(f):

        key.dt = 0.02/f

        key.T0 = (key.F+key.W)/U

        if pi.Re > TDREH:
            key.et = 6*key.T0
            key.wt = 0.1
        else:
            et = key.T0+0.3
            wt = 0.1

        # Same here : NEEDS TO BE INT
        # these ar for feeding into the string in blockMeshDict_utils.py
        key.AAA = np.array([1*f, 2*f, 1]).astype(str)
        key.BBB = np.array([3*f, 2*f, 1]).astype(str)
        key.CCC = np.array([3*f, 3*f, 1]).astype(str)
        key.DDD = np.array([2*f, 3*f, 1]).astype(str)
        key.EEE = np.array([int(1.5*f), 3*f, 1]).astype(str)
        key.FFF = np.array([int(1.5*f), 2*f, 1]).astype(str)
    updateKey(key.f)

    # param defaults

    cylwallpoints = cyw.cylwall(key.R, key.f)
    cylpi4 = cyw.cylnorm(key.R, np.pi/4)
    cylpi2 = cyw.cylnorm(key.R, np.pi/2)
    cyl3pi4 = cyw.cylnorm(key.R, 3*np.pi/4)

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
                'n': key.cores
            },

            {
                'probeLocations': '\n    (5.5 0.5 0)\n    (5.5 -0.5 0)',
            },

            {
                'recirculation':
                f"""\n        \tstart   (0.5 0 0);
                end     ({str(key.W)} 0 0);
                    """,
                # 'cylwall':
                # f"""\n\tpoints   ({cylwallpoints});
                #     """,
                'cylnormal_pi4':
                f"""\n\tstart   ({cylpi4[0]});\n\tend     ({cylpi4[1]});
                    """,
                'cylnormal_pi2':
                f"""\n\tstart   ({cylpi2[0]});\n\tend     ({cylpi2[1]});
                    """,
                'cylnormal_3pi4':
                f"""\n\tstart   ({cyl3pi4[0]});\n\tend     ({cyl3pi4[1]});
                    """,
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
