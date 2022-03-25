import numpy as np
import pandas as pd
from scipy import signal as sig
import re


def main():
    # ------------------- DATA PARSING -------------------
    path = "/home/mandy/Downloads/"        # File path to the file
    file_name = "Test"                                            # Name of file
    data = path + file_name


    with open(data) as lines:
        for line in lines:
            print(line)

    # ------------------- Fourier Transform -------------------
    # Using fourier transform of data to calculate frequency
    Yu = df['uy1'].to_numpy()   # Change datatype to np array
    Yu = np.fft.fft(Yu)         # Fourier transform Y

    # ------------------- Filter -------------------
    peak_location = sig.find_peaks(Yu)      # find locations of peaks so we may find frequency! (FREQUENCY IS X DOMAIN)
    peak_min = 0                            # [Hz] Filter out any frequencies lower than this
    peak_max = 100                          # [Hz] Filter out any frequencies higher than this
    Yu_filtered = Yu[Yu < peak_max]
    Yu_filtered = Yu[Yu > peak_min]

    # ------------------- Get variables ! -------------------
    fs = 100            # [Hz] Samples collected per second
    ts = 1.0 / fs       # [s] Time step
    N = len(Yu)         # Number of samples
    f0 = Yu_filtered    # [Hz] Frequency obtained from fourier transform
    D = 1               # [m OR dimensionless] Diameter of Cylinder
    U = 1               # [m/s OR dimensionless] Velocity of Freestream

    # ------------------- Strouhal number Calculation -------------------
    St = f0 * D / U     # [dimensionless] Strouhal Number

    return


main()
