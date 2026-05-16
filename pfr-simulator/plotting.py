# plotting.py

from turtle import lt
import matplotlib.pyplot as plt
import numpy as np
from reactor_model import reaction_rate
from parameters import CA0


def set_plot_style():
    plt.rcParams.update({
        "figure.figsize": (6,4),
        "figure.dpi": 120,

        "font.size": 11,
        "axes.titlesize": 12,
        "axes.labelsize": 11,

        "axes.linewidth": 1.1,

        "lines.linewidth": 2,

        "legend.frameon": False,
        "legend.fontsize": 10,

        "grid.alpha": 0.3,

        "xtick.direction": "in",
        "ytick.direction": "in"
    })


def plot_concentration(V, CA, CA2, N, cstr_train_V, cstr_train_CA):

    set_plot_style()
    plt.figure()

    plt.plot(V, CA, label="PFR", linewidth=2.5)
    plt.plot(V, CA2, label="CSTR", linewidth=2.5)
    plt.plot(cstr_train_V, cstr_train_CA,
             marker='o',
             markersize=4,
             linestyle='-',
             label=f"CSTR Train (N={N})")
    plt.xlabel("Reactor Volume (L)")
    plt.ylabel("Concentration of A (mol/L)")
    plt.title("Concentration Profile in Reactors")

    plt.text(
    0.05, 0.95,
    "CSTR train → PFR (N increases)",
    transform=plt.gca().transAxes,
    fontsize=9,
    style='italic',
    bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.7)
    )
    
    plt.legend()
    plt.grid()

    plt.tight_layout()
    plt.savefig("example_plots/concentration_profile.png", dpi=300)

    plt.show()


def plot_conversion(V, CA, CA2, CA0):
    
    set_plot_style()
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
    plt.savefig("example_plots/conversion_profile.png", dpi=300)

    plt.show()


def levenspiel(X_out):
    
    set_plot_style()
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
        linestyle="--",
        color="green")

    plt.plot([0, X_out],
        [1/(-rA_out), 1/(-rA_out)],
        linestyle="--",
        color="green",
        label="CSTR")
    plt.xlabel("Conversion, X")
    plt.ylabel("1 / (-rA)")
    plt.title("Levenspiel Plot for PFR vs CSTR Design")
    plt.legend()
    
    plt.tight_layout()
    plt.savefig("example_plots/levenspiel_plot.png", dpi=300)
    
    plt.show()
    

