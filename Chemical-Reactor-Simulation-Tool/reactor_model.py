# reactor_model.py

from parameters import k, FA0
from scipy.optimize import fsolve

def reaction_rate(CA):
    """
    Calculates reaction rate using first order kinetics.

    rA = -k * CA

    CA : concentration of A
    k  : reaction rate constant
    """

    rA = -k * CA
    return rA


def solve_pfr(V, CA):
    """
    Differential equation for a Plug Flow Reactor.

    dCA/dV = rA / FA0

    V   : reactor volume
    CA  : concentration of A
    """

    rA = reaction_rate(CA)

    dCAdV = rA / FA0

    return dCAdV


def solve_cstr(CA0, FA0, V):
    """
    Solves the CSTR design equation numerically.

    CA0 : inlet concentration
    FA0 : inlet molar flow rate
    V   : reactor volume
    """

    def equation(CA):
        rA = reaction_rate(CA)
        return CA0 + (rA * V) / FA0 - CA

    CA_guess = CA0 * 0.5

    CA_solution = fsolve(equation, CA_guess)

    return CA_solution[0]


def solve_cstr_train(CA0, FA0, V_total, N):
    """
    CSTR train model (PFR approximation using N CSTRs in series)
    """

    dV = V_total / N
    CA = CA0

    CA_profile = [CA0]

    for i in range(N):

        rA = reaction_rate(CA)

        # CSTR mole balance:
        # FA0(CA_in - CA_out) = -rA * V
        CA = CA + (rA * dV) / FA0

        CA_profile.append(CA)

    return CA_profile