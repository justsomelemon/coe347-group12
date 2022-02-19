#!usr/bin/python3
from matplotlib import pyplot as plt
import numpy as np
import jpcm
from scipy.optimize import curve_fit

from utils import *

tmfile = f'{datapath}time/time.txt'
plotfile = f'{plotdir}time.jpg'

T = 0.5
deltaT = np.array([0.005, 0.0025, 0.00125, 0.000625])
step = T/deltaT
N = np.power(np.array([20, 40, 80, 160]), 2)

with open(tmfile, 'r') as file:
    text = file.read()

lines = text.split('\n')

times = np.array([float(line.split('user')[0])
                 for line in lines if 'user' in line][:4])

C = times/step


def f(x, a, b):
    return b*np.power(x, a)


popt, pcov = curve_fit(f, N, C)

x_fit = np.linspace(min(N), max(N), 100)
y_fit = f(x_fit, popt[0], popt[1])
plt.loglog(N, C, c=jpcm.maps.ginshu, label='data')
plt.loglog(x_fit, y_fit, c=jpcm.maps.rurikon,
           label='fit: exponent={}'.format(popt[0]))
plt.title("Refinement Time (C vs N)")
plt.xlabel("Grid Points [N]")
plt.ylabel("Wallclock Time / Step [s]")
plt.legend()
plt.savefig(plotfile)
plt.close()
