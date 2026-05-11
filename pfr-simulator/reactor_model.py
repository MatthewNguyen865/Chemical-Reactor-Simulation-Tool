# reactor_model.py

from parameters import k, FA0

def reaction_rate(CA):
    """
    Calculates reaction rate using first order kinetics.

    rA = -k * CA

    CA : concentration of A
    k  : reaction rate constant
    """

    rA = -k * CA
    return rA


def dCAdV(V, CA):
    """
    Differential equation for a Plug Flow Reactor.

    dCA/dV = rA / FA0

    V   : reactor volume
    CA  : concentration of A
    """

    rA = reaction_rate(CA)

    dCAdV = rA / FA0

    return dCAdV
