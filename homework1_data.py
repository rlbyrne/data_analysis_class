#!/usr/bin/python

import numpy as np
import matplotlib.pyplot as plt
import scipy.io


def plot_gain_solutions():

    sav = scipy.io.readsav('/Users/ruby/Documents/2018 Fall Quarter/phys576b/homework1/hex_array_sim_331_cal.sav')
    cal_gains = np.zeros(
        (2,
         np.shape(sav['cal']['gain'][0][0])[0],
         np.shape(sav['cal']['gain'][0][0])[1]
         ),
        dtype=complex)
    cal_gains[0, :, :] = sav['cal']['gain'][0][0]
    cal_gains[1, :, :] = sav['cal']['gain'][0][1]

    hist, bin_edges = np.histogram(np.abs(cal_gains), bins=20)
    plot_y = [val for val in hist for null in [0, 1]]
    plot_x = ([val for val in bin_edges for null in [0, 1]])[1:-1]
    print(np.sum(hist))
    plt.semilogy(plot_x, plot_y)
    plt.xlabel('gain amplitude')
    plt.ylabel('count')
    plt.title('Hex Array Gain Amplitude Histogram: All Antennas and Frequencies')
    plt.savefig('/Users/ruby/Documents/2018 Fall Quarter/phys576b/homework1/all_gains_hist.png')
    plt.close()

    hist_across_freq = np.zeros((len(hist), np.shape(cal_gains)[2]))
    for freq in range(np.shape(cal_gains)[2]):
        hist, bin_edges = np.histogram(np.abs(cal_gains[:, :, freq]),
                                       bins=bin_edges)
        hist_across_freq[:, freq] = hist

    plt.imshow(
        hist_across_freq.T, origin='lower', interpolation='none',
        extent=[bin_edges[0], bin_edges[-1], 0, np.shape(cal_gains)[2]])
    plt.axes().set_aspect('auto')
    plt.xlabel('gain amplitude')
    plt.ylabel('frequency channel')
    cbar = plt.colorbar()
    cbar.ax.set_ylabel('histogram counts', rotation=270)
    plt.savefig('/Users/ruby/Documents/2018 Fall Quarter/phys576b/homework1/gains_hist_vs_freq.png')
    plt.close()


if __name__=='__main__':
    plot_gain_solutions()
