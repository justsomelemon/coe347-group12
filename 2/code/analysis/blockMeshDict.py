# from matplotlib import pyplot as plt
import numpy as np

import blockMeshDict_utils as bmut

nP = 3  # don't change for now, it doesn't work properly yet!
nSector = 2**nP  # must be a power of 2, greater than 8!
nV = nSector*6 + 16


# test

def gen(key):
    # blockFactor = pi.Re
    # R = L/2
    # H = 4
    # F = 4
    # W = 4 + pi.Re*(1/10)

    # Vertices

    def vertOut(p): return f'({p[0]} {p[1]} {p[2]}) \t\t// {p[3]}'

    vs = np.zeros(shape=(nV, 4))
    vs[:int(nV/2), 2] = -key.K
    vs[int(nV/2):, 2] = key.K
    vs[:, 3] = list(range(nV))

    # circular

    theta = 2*np.pi*np.array(range(nSector))/nSector
    c = np.cos(theta)
    s = np.sin(theta)

    vs[:nSector, 0] = key.R*c
    vs[:nSector, 1] = key.R*s
    ox = key.R2*c
    oy = key.R2*s
    vs[nSector:2*nSector, 0] = ox
    vs[nSector:2*nSector, 1] = oy

    vs[2*nSector:2*nSector+nP, 0] = np.full(shape=(nP), fill_value=key.W)
    vs[2*nSector:2*nSector+nP-1, 1] = oy[:nP-1]
    vs[2*nSector+nP-1, 1] = key.H

    vs[int(2.5*nSector)-(nP-2):int(2.5*nSector)+nP,
       1] = np.full(shape=(2*nP-2), fill_value=key.H)
    vs[int(2.5*nSector)-(nP-2):int(2.5*nSector)+nP-1,
       0] = ox[nP-2:2*nP-2]
    vs[int(2.5*nSector)+nP-1, 0] = -key.F

    vs[int(3*nSector)-(nP-2):int(3*nSector)+nP,
       0] = np.full(shape=(2*nP-2), fill_value=-key.F)
    vs[int(3*nSector)-(nP-2):int(3*nSector)+nP-1,
       1] = oy[2*nP-3:3*nP-3]
    vs[int(3*nSector)+nP-1, 1] = -key.H

    vs[int(3.5*nSector)-(nP-2):int(3.5*nSector)+nP,
       1] = np.full(shape=(2*nP-2), fill_value=-key.H)
    vs[int(3.5*nSector)-(nP-2):int(3.5*nSector)+nP-1,
       0] = ox[3*nP-4:4*nP-4]
    vs[int(3.5*nSector)+nP-1, 0] = key.W

    vs[int(4*nSector)-(nP-2):int(4*nSector),
       0] = np.full(shape=(nP-2), fill_value=key.W)
    vs[int(4*nSector)-(nP-2):int(4*nSector), 1] = oy[4*nP-5:5*nP-7]

    vs[int(nV/2):, 0] = vs[:int(nV/2), 0]
    vs[int(nV/2):, 1] = vs[:int(nV/2), 1]

    # z = vs[:, 0]
    # y = vs[:, 1]
    # n = vs[:, 3]

    # plt.scatter(z, y)
    # for i, txt in enumerate(n):
    #     plt.annotate(txt, (z[i], y[i]))
    # plt.show()

    vert = "\n\t".join([vertOut(p) for p in vs])

    # Blocks

    # def block(p): return f'({p[0]} {p[1]} {p[3]}) \t\t// {p[4]}'
    bt = bmut.blocktext.replace('AAA', " ".join(key.AAA))
    bt = bt.replace('BBB', " ".join(key.BBB))
    bt = bt.replace('CCC', " ".join(key.CCC))
    bt = bt.replace('DDD', " ".join(key.DDD))
    bt = bt.replace('EEE', " ".join(key.EEE))
    bt = bt.replace('FFF', " ".join(key.FFF))

    # Arcs

    def arcOut(a, b, p): return f"arc {a} {b} ({p[0]} {p[1]} {p[2]})"

    def getPt(vs, idx, t):
        # assuming same z,R
        p1 = vs[idx]
        R = np.sqrt(p1[0]**2 + p1[1]**2)
        return [R*np.cos(t), R*np.sin(t), p1[2]]

    data = np.zeros(shape=(nSector*4, 2), dtype=np.int32)
    pts = np.zeros(shape=(nSector*4, 3))

    id = 0
    t2 = 2*np.pi*((1/(2*nSector)) + np.array(range(nSector))/nSector)
    for j in [0, nSector, int(nV/2), int(nV/2)+nSector]:
        for i in range(nSector):
            idx = i+j
            idx2 = ((i+1) % nSector) + j
            data[id, 0] = idx
            data[id, 1] = idx2
            pts[id, :] = getPt(vs, idx, t2[i])

            id += 1

    e = "\n\t".join([arcOut(q[0], q[1], p) for q, p in zip(data, pts)])

    return vert, bt, e


def replace(txt, data):
    v, b, e = data
    txt = txt.replace('VVV', v)
    txt = txt.replace('BBB', b)
    txt = txt.replace('EEE', e)
    return txt


def generate(path, param):
    with open(path, 'r') as file:
        txt = file.read()
    data = gen(param)
    txt = replace(txt, data)
    with open(path, 'w') as file:
        file.write(txt)
