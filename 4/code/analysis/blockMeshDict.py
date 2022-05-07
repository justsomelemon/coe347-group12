# from matplotlib import pyplot as plt
import numpy as np


def replace(txt, k):
    scale = 20
    txt = txt.replace('BM_A', str(int(scale*k.m * k.f)))
    txt = txt.replace('BM_B', str(int(scale*k.H * k.f)))
    txt = txt.replace('BM_C', str(int(scale*k.r * k.f)))
    txt = txt.replace('BM_D', str(int(scale*k.a * k.f)))
    txt = txt.replace('BM_E', str(int(scale*k.w * k.f)))
    txt = txt.replace('BM_F', str(int(scale*2*k.e * k.f)))
    txt = txt.replace('dim_L', str(k.L))
    txt = txt.replace('dim_H', str(k.H))
    txt = txt.replace('dim_m', str(k.m))
    txt = txt.replace('dim_n', str(k.n))
    txt = txt.replace('dim_p', str(k.p))
    txt = txt.replace('dim_q', str(k.q))
    txt = txt.replace('dim_r', str(k.r))
    return txt


def generate(path, param):
    with open(path, 'r') as file:
        txt = file.read()
    txt = replace(txt, param)
    # print(txt)
    with open(path, 'w') as file:
        file.write(txt)
