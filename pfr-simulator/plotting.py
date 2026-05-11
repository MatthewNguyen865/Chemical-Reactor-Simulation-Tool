# plotting.py

import matplotlib.pyplot as plt


def plot_concentration(V, CA):
    """
    Plots concentration of A along the reactor volume.
    """

    plt.figure()

    plt.plot(V, CA)

    plt.xlabel("Reactor Volume (L)")
    plt.ylabel("Concentration of A (mol/L)")
    plt.title("Concentration Profile in Plug Flow Reactor")

    plt.show()


def plot_conversion(V, CA, CA0):
    """
    Plots conversion of A along the reactor.
    """

    X = (CA0 - CA) / CA0

    plt.figure()

    plt.plot(V, X)

    plt.xlabel("Reactor Volume (L)")
    plt.ylabel("Conversion of A")
    plt.title("Conversion vs Reactor Volume")

    plt.show()
