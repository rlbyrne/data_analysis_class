#!/usr/bin/python

import scipy.stats
import scipy.special
import numpy as np
import matplotlib.pyplot as plt


def create_poisson_dist():

    n_points=100000
    data_array = np.random.poisson(lam=50.1, size=n_points)
    hist, bin_edges = np.histogram(data_array, bins=20)
    plot_y = [val for val in hist for null in [0, 1]]
    plot_x = ([val for val in bin_edges for null in [0, 1]])[1:-1]
    plt.semilogy(plot_x, plot_y)
    plt.xlabel('counts')
    plt.ylabel('number of instances')
    plt.title('Poisson Distribution Histogram')
    plt.savefig('/Users/ruby/Documents/2018 Fall Quarter/phys576b/homework1/poisson_hist.png')
    plt.close()

    plot_y_norm = plot_y/np.sum(hist)
    plt.semilogy(plot_x, plot_y_norm)
    plt.xlabel('counts')
    plt.ylabel('probability')
    plt.title('Normalized Poisson Distribution Histogram')
    plt.savefig('/Users/ruby/Documents/2018 Fall Quarter/phys576b/homework1/poisson_hist_norm.png')
    plt.close()

    print(scipy.stats.poisson.cdf(80, 50.1))
    print(1.-scipy.stats.poisson.cdf(30, 50.1))
    print(scipy.special.erfinv(scipy.stats.poisson.cdf(80, 50.1)))
    print(scipy.special.erfinv(1.-scipy.stats.poisson.cdf(30, 50.1)))


def create_2d_gaussian_dist():

    n_points=100000
    data_array_x = np.random.normal(size=n_points)
    data_array_y = np.random.normal(size=n_points)
    data_length = [
        (data_array_x[i]**2+data_array_y[i]**2)**.5 for i in range(n_points)
        ]
    hist, bin_edges = np.histogram(data_length, bins=20)
    plot_y = [val for val in hist for null in [0, 1]]
    plot_x = ([val for val in bin_edges for null in [0, 1]])[1:-1]
    plot_y = plot_y/np.sum(hist)
    plt.semilogy(plot_x, plot_y)
    plt.xlabel('counts')
    plt.ylabel('number of instances')
    plt.title('2D Gaussian Amplitude Distribution Histogram (Normalized)')
    plt.savefig('/Users/ruby/Documents/2018 Fall Quarter/phys576b/homework1/2d_gaussian_dist_equal_var.png')
    plt.close()

    data_array_y = np.random.normal(scale=10, size=n_points)
    data_length = [
        (data_array_x[i]**2+data_array_y[i]**2)**.5 for i in range(n_points)
        ]
    hist, bin_edges = np.histogram(data_length, bins=20)
    plot_y = [val for val in hist for null in [0, 1]]
    plot_x = ([val for val in bin_edges for null in [0, 1]])[1:-1]
    plot_y = plot_y/np.sum(hist)
    plt.semilogy(plot_x, plot_y)
    plt.xlabel('counts')
    plt.ylabel('number of instances')
    plt.title('2D Gaussian Amplitude Distribution Histogram (Normalized)')
    plt.savefig('/Users/ruby/Documents/2018 Fall Quarter/phys576b/homework1/2d_gaussian_dist_unequal_var.png')
    plt.close()

    # get bin edges
    null, bin_edges = np.histogram(np.concatenate((data_array_x, data_array_y)), bins=20)
    hist2d, xedges, yedges = np.histogram2d(data_array_x, data_array_y, bins=bin_edges)
    plt.imshow(
        (hist2d/np.sum(hist2d)).T, origin='lower', interpolation='none',
        extent=[xedges[0], xedges[-1], yedges[0], yedges[-1]], aspect=1)
    plt.xlabel('x length')
    plt.ylabel('y length')
    cbar = plt.colorbar()
    cbar.ax.set_ylabel('Probability Density', rotation=270)
    plt.savefig('/Users/ruby/Documents/2018 Fall Quarter/phys576b/homework1/2d_gaussian_2d_hist.png')
    plt.close()






if __name__=='__main__':
    create_2d_gaussian_dist()
