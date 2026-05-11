# main.py

import numpy as np
from scipy.integrate import solve_ivp

from reactor_model import dCAdV
from plotting import plot_concentration, plot_conversion
from parameters import CA0, V_final


print("Plug Flow Reactor Simulation")
print("----------------------------")
print("Reaction: A → B")
print("Rate law: rA = -kCA")


# Solve reactor differential equation

V_span = (0, V_final)

V_eval = np.linspace(0, V_final, 100)

solution = solve_ivp(dCAdV, V_span, [CA0], t_eval=V_eval)

V = solution.t
CA = solution.y[0]


print("Simulation complete.")
print("Final concentration of A:", CA[-1])


# Plot results

plot_concentration(V, CA)

plot_conversion(V, CA, CA0)
