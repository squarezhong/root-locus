import argparse
import control
import numpy as np
from matplotlib import pyplot as plt

def get_roots():
    CLI=argparse.ArgumentParser()
    CLI.add_argument("--num", nargs="+", type=float, default=[1, 2, 3])
    CLI.add_argument("--den", nargs="+", type=float, default=[3, 5, 7])
    args = CLI.parse_args()

    numerator = args.num
    denominator = args.den

    zeros = np.roots(numerator)
    poles = np.roots(denominator)

    tf = control.TransferFunction(numerator, denominator)
    roots, gains = control.root_locus(tf, kvect=np.linspace(0.0, 20.0, num=500),plot=False)
    return zeros, poles, roots, gains

def plot_root_locus(zeros, poles, roots, gains):
    reals = np.real(roots)
    imags = np.imag(roots)

    colors = ['b', 'm', 'c', 'r', 'g']

    fig, ax = plt.subplots()
    ax.set_xlabel('Re')
    ax.set_ylabel('Im')
    ax.axvline(x=0, color='k', lw=1)
    ax.grid(True)

    # plot poles and zeros
    ax.scatter(np.real(poles), np.imag(poles), marker='x', color='b')
    ax.scatter(np.real(zeros), np.imag(zeros), marker='o', color='r', facecolors='none')

    # plot root locus with different colors
    for index, (r, i) in enumerate(zip(reals.T, imags.T)):
        ax.plot(r, i, color=colors[index%len(colors)])

    plt.show()

    return fig, ax

if __name__ == "__main__":
    zeros, poles, roots, gains = get_roots()
    plot_root_locus(zeros, poles, roots, gains)
