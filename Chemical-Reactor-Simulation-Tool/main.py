# main.py

import numpy as np
from scipy.integrate import solve_ivp
from reactor_model import solve_pfr, solve_cstr, solve_cstr_train
from plotting import plot_concentration, plot_conversion, levenspiel
from parameters import CA0, V_final, FA0

import os
os.makedirs("example_plots", exist_ok=True)

print("PFR and CSTR Simulation")
print("----------------------------")
print("Reaction: A → B")
print("Rate law: rA = -kCA")

# Solve reactor equations

V_span = (0, V_final)

V_eval = np.linspace(0, V_final, 100)

pfr_solution = solve_ivp(solve_pfr, V_span, [CA0], t_eval=V_eval)
cstr_CA= []
for V in V_eval:
    CA_exit_cstr = solve_cstr(CA0, FA0, V)
    cstr_CA.append(CA_exit_cstr)

pfr_V = pfr_solution.t
pfr_CA = pfr_solution.y[0]

# CSTR train approximates pfr with N CSTRs in series

N = 10  # number of tanks in CSTR train
cstr_train_CA = solve_cstr_train(CA0, FA0, V_final, N)
cstr_train_V = np.linspace(0, V_final, N+1)

# Print results

print("Simulation complete.")
print("Final PFR concentration:", f"{pfr_CA[-1]:.4f}")
print("Final PFR conversion:", f"{(CA0 - pfr_CA[-1]) / CA0:.4f}")
print("Final CSTR concentration:", f"{cstr_CA[-1]:.4f}")
print("Final CSTR conversion:", f"{(CA0 - cstr_CA[-1]) / CA0:.4f}")

# Plot results

plot_concentration(pfr_V, pfr_CA, cstr_CA, N, cstr_train_V, cstr_train_CA)

plot_conversion(pfr_V, pfr_CA, np.array(cstr_CA), CA0)

# Levenspiel plot

Cstr_X_out = (CA0 - cstr_CA[-1]) / CA0
levenspiel(Cstr_X_out)
