"""working with figures"""

import numpy as np
import matplotlib.patches as patches
import matplotlib.pyplot as plt

def plot1():
    """compositing multiple figures"""
    T = np.linspace(-np.pi, np.pi, 1024)
    grid_size = (4, 2)
    # define a grid of 4 rows and 2 cols
    plt.subplot2grid(grid_size, (0, 0), rowspan=3, colspan=1)
    plt.plot(np.sin(2 * T), np.cos(0.5 * T), c='k')

    plt.subplot2grid(grid_size, (0, 1), rowspan=3, colspan=1)
    plt.plot(np.cos(3 * T), np.sin(T), c='k')

    plt.subplot2grid(grid_size, (3, 0), rowspan=1, colspan=3)
    plt.plot(np.cos(5 * T), np.sin(7 * T), c='k')

    plt.tight_layout()
    plt.show()

def get_radius(T, params):
    """get_radius"""
    m, n_1, n_2, n_3 = params
    U = (m * T) / 4
    return (np.fabs(np.cos(U)) ** n_2 + np.fabs(np.sin(U)) ** n_3) ** (-1. / n_1)

def plot2():
    """add title to each subfigure"""
    grid_size = (3, 4)
    T = np.linspace(0, 2 * np.pi, 1024)

    for i in range(grid_size[0]):
        for j in range(grid_size[1]):
            params = np.random.random_integers(1, 20, size=4)
            R = get_radius(T, params)

            axes = plt.subplot2grid(grid_size, (i, j), rowspan=1, colspan=1)
            axes.get_xaxis().set_visible(False)
            axes.get_yaxis().set_visible(False)

            plt.plot(R * np.cos(T), R * np.sin(T), c='k')
            plt.title('%d, %d, %d, %d' % tuple(params), fontsize='small')

    plt.tight_layout()
    plt.show()

def plot3():
    """an alternative way to composite figures"""
    T = np.linspace(-np.pi, np.pi, 1024)
    fig, (ax0, ax1) = plt.subplots(ncols=2)
    ax0.plot(np.sin(2 * T), np.cos(0.5 * T), c='k')
    ax1.plot(np.cos(3 * T), np.sin(T), c='k')
    plt.show()

def plot4():
    """scaling both the axes equally"""
    T = np.linspace(0, 2 * np.pi, 1024)
    # plt.plot(2. * np.cos(T), np.sin(T), c='k', lw=3.)
    plt.plot(np.cos(T), 2. * np.sin(T), c='k', lw=3.)
    plt.axes().set_aspect('equal')
    plt.show()

def plot5():
    """setting an axis range"""
    X = np.linspace(-6, 6, 2014)
    plt.ylim(-.5, 1.5)
    plt.plot(X, np.sinc(X), c='k')
    plt.show()

def plot6():
    """setting the aspect ratio"""
    X = np.linspace(-6, 6, 1024)
    Y1, Y2 = np.sinc(X), np.cos(X)

    plt.figure(figsize=(10.24, 2.56))
    plt.plot(X, Y2, c='.75', lw=3.)
    plt.plot(X, Y1, c='k', lw=3.)
    plt.show()

def plot7():
    """inserting subfigures"""
    X = np.linspace(-6, 6, 1024)
    Y = np.sinc(X)

    X_detail = np.linspace(-3, 3, 1024)
    Y_detail = np.sinc(X_detail)

    plt.plot(X, Y, c='k')
    sub_axes = plt.axes([.6, .6, .25, .25])
    sub_axes.plot(X_detail, Y_detail, c='k')
    plt.setp(sub_axes)
    plt.show()

def plot8():
    """using a logarithmic scale"""
    X = np.linspace(1, 10, 1024)
    plt.yscale('log')
    plt.plot(X, X, c='k', lw=2., label=r'$f(x)=x$')
    plt.plot(X, 10 ** X, c='.75', ls='--', lw=2., label=r'$f(x)=e^x$')
    plt.plot(X, np.log(X), c='.75', lw=2., label=r'$f(x)=\log(x)$')
    plt.legend()
    plt.show()

def plot9():
    """symlog"""
    X = np.linspace(-100, 100, 4096)
    plt.xscale('symlog', linthreshx=6.)
    plt.plot(X, np.sinc(X), c='k')
    plt.show()

def plot10():
    """using polar coordinates"""
    T = np.linspace(0, 2 * np.pi, 1024)
    plt.axes(polar=True)
    plt.plot(T, 1. + .25 * np.sin(16 * T), c='k')
    plt.show()

def plot11():
    """ploar"""
    ax = plt.axes(polar=True)
    theta = np.linspace(0, 2 * np.pi, 8, endpoint=False)
    radius = .25 + .75 * np.random.random(size=len(theta))
    points = np.vstack((theta, radius)).transpose()
    plt.gca().add_patch(patches.Polygon(points, color='.75'))
    plt.show()

plot11()
