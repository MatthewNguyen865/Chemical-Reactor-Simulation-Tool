# plotting.py

from turtle import lt
import matplotlib.pyplot as plt
import numpy as np
from reactor_model import reaction_rate
from parameters import CA0


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


def levenspiel(X_out):
    """
    Plots the Levenspiel plot for the pfr and cstr.
    """
    X = np.linspace(0, 0.99, 200)
    CA = CA0 * (1 - X)
    rA = reaction_rate(CA)

    plt.figure(figsize=(7, 5))
    plt.grid(True, alpha=0.3)
    plt.plot(X, 1/(-rA), linewidth=2)
    plt.fill_between(X, 1/(-rA), alpha=0.2, label="PFR (area)")

    CA_out = CA0 * (1 - X_out)
    rA_out = reaction_rate(CA_out)

    plt.plot([X_out, X_out],
        [0, 1/(-rA_out)],
        linestyle="--")

    plt.plot([0, X_out],
        [1/(-rA_out), 1/(-rA_out)],
        linestyle="--",
        label="CSTR")
    plt.xlabel("Conversion, X")
    plt.ylabel("1 / (-rA)")
    plt.title("Levenspiel Plot for PFR vs CSTR Design")
    plt.legend()
    plt.tight_layout()
    
    plt.show()
    