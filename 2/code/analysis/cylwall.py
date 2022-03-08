import numpy as np


def cylwall(R, blockFactor):
    n = 10
    theta = np.linspace(0, 2*np.pi, n)
    x = R*np.cos(theta)
    y = R*np.sin(theta)
    return " ".join([f"({x[i]} {y[i]} 0)" for i in range(n)])


def cylnorm(R, theta, l=3):
    c = np.cos(theta)
    s = np.sin(theta)
    start = f"{R*c} {R*s} 0"
    end = f"{(R+l)*c} {(R+l)*s} 0"
    return start, end
