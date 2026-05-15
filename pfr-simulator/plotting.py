# plotting.py

import matplotlib.pyplot as plt


def plot_concentration(V, CA, CA2):
    """
    Plots concentration of A along the reactor volume.
    """

    plt.figure()

    plt.plot(V, CA, label="PFR")
    plt.plot(V, CA2, label="CSTR")

    plt.xlabel("Reactor Volume (L)")
    plt.ylabel("Concentration of A (mol/L)")
    plt.title("Concentration Profile in Plug Flow Reactor")
    plt.legend()

    plt.tight_layout()
    plt.show()


def plot_conversion(V, CA, CA2, CA0):
    """
    Plots conversion of A along the reactor.
    """

    X = (CA0 - CA) / CA0
    X2 = (CA0 - CA2) / CA0

    plt.figure()

    plt.plot(V, X, label="PFR")
    plt.plot(V, X2, label="CSTR")

    plt.xlabel("Reactor Volume (L)")
    plt.ylabel("Conversion of A")
    plt.title("Conversion vs Reactor Volume")
    plt.legend()

    plt.tight_layout()
    plt.show()
