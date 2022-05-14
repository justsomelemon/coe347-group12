from ast import literal_eval as make_tuple
import os
import pandas as pd
from scipy import signal as sig
import matplotlib.pyplot as plt
import numpy as np
import jpcm


def main():
    # ------------------- DATA PARSING -------------------
    path = 'data/'
    plpath = '../plots/'
    denylist = ['.gitignore']
    files = os.listdir(path)
    # Formatting of name: mesh factor, Re, wall thickness, window width
    for file in files:
        if file not in denylist:
            print(file)
            data = path + file + '/postProcessing/probes/0/U'

            df = pd.read_csv(data, sep='             ', header=None, names=[
                'Time', 'Probe 0', 'Probe 1'], engine='python')

            df = df.drop([0, 1, 2, 3])

            uy0 = np.array([make_tuple(val.replace(' ', ','))
                           for val in df['Probe 0']])
            uy1 = np.array([make_tuple(val.replace(' ', ','))
                            for val in df['Probe 1']])

            time = [float(val) for val in df['Time']]
            us = [uy0, uy1]
            for i in range(2):  # probes

                # ------------------- Fourier Transform -------------------
                # Using fourier transform of data to calculate frequency

                t0 = np.array(time)
                x = np.array(us[i][:, 1])
                assert len(t0) == len(x)
                # X = np.fft.fft(us[i])  # Fourier transform
                f, t, Zxx = sig.stft(x, fs=1/(t0[1]-t0[0]), nperseg=10)
                mx = np.max(np.abs(Zxx), axis=0)
                # # ------------------- Filter -------------------
                # p = 100
                # peak_location = [[]]
                # while not peak_location[0]:
                #     p -= 1
                #     # find locations of peaks so we may find
                #     peak_location = sig.find_peaks(X, prominence=p)
                # # frequency! (FREQUENCY IS X DOMAIN)

                # # Frequency will be LOW frequency
                # # For some reason indices seem to be 1 lower?
                # Yu_filtered = abs(np.abs(freq[min(peak_location[0]) + 1]))
                # # ------------------- Get variables ! -------------------
                # fs = 10  # [Hz] Samples collected per second
                # ts = 1.0 / fs  # [s] Time step
                # N = len(X)  # Number of samples
                # f0 = Yu_filtered  # [Hz] Frequency obtained from fourier transform
                # D = 1  # [m OR dimensionless] Diameter of Cylinder
                # U = 1  # [m/s OR dimensionless] Velocity of Freestream

                # # ------------------- Strouhal number Calculation -------------------
                # St = f0 * D / U  # [dimensionless] Strouhal Number
                # print(f'Strouhal Number at Probe {i}:', St)

                # ------------------- PLOTS -------------------
                plt.figure(figsize=(8, 6))
                plt.plot(t0, x, 'r')
                plt.ylabel('Velocity (Uy)')
                plt.xlabel('Time')
                plt.title('Uy vs Time Probe 0 ' + file)
                plt.savefig(f'{plpath}{file}/probe{i}.png')
                plt.close()

                plt.figure(figsize=(8, 6))
                im = plt.pcolormesh(t, f, np.abs(Zxx), vmin=0,
                                    vmax=np.max(np.abs(Zxx)), shading='gouraud', cmap=jpcm.get('fuyu'))
                plt.plot(t, mx, c=jpcm.maps.karakurenai)
                idx = t[np.argmax(mx)]
                plt.text(idx, -.125, f'{idx:.3f}',
                         color='red', ha='center', va='top')

                plt.ylim([0, 2])
                plt.legend(['Fundamental'])
                plt.ylabel('Frequency [St - ndl]')
                plt.xlabel('Time [ndl]')
                plt.title(
                    f'FFT Plot of Vortex Shedding Frequency Probe {i} : ' + file)
                plt.colorbar(im)
                plt.savefig(f'{plpath}{file}/probe_FFT{i}.png')
                plt.close()


main()
