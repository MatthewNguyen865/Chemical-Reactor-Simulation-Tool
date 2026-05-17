# Chemical Reactor Simulation Tool

Example reactor concentration profile:

![Concentration Plot](example_plots/concentration_plot.png)

The concentration profile of reactant A along reactor volume for three reactor configurations: an ideal Plug Flow Reactor (PFR), a single Continuous Stirred Tank Reactor (CSTR), and a series of CSTRs approximating plug flow behavior. As the number of tanks in the CSTR train increases, the system approaches the performance of a PFR.

A Python-based simulation of ideal chemical reactors used in chemical reaction engineering.  
The project numerically models **Plug Flow Reactors (PFR)**, **Continuous Stirred Tank Reactors (CSTR)**, and **CSTR trains**, and visualizes reactor performance using engineering plots including a **Levenspiel diagram**.

This project demonstrates how core chemical engineering reactor design equations can be implemented using numerical methods and scientific computing in Python.

---

# Overview

Chemical reactors are fundamental units in chemical engineering used to convert reactants into products. Different reactor designs lead to different performance characteristics.

This simulation models and compares three ideal reactor configurations:

• Plug Flow Reactor (PFR)  
• Continuous Stirred Tank Reactor (CSTR)  
• CSTR train (series of CSTRs approximating a PFR)

The model solves the governing reactor equations numerically and visualizes concentration profiles, conversion, and reactor design relationships.

---

# Reaction System

Reaction:

A → B

First-order reaction kinetics:

rA = -k · CA

Where:

- rA = reaction rate (mol/L·s)
- k = rate constant (1/s)
- CA = concentration of species A (mol/L)

---

# Reactor Models

## Plug Flow Reactor (PFR)

The PFR design equation:

dFA / dV = rA

For constant volumetric flow rate:

dCA / dV = rA / v0

This differential equation is solved numerically using the ODE solver from SciPy.

---

## Continuous Stirred Tank Reactor (CSTR)

For a steady-state CSTR:

FA0 - FA + rA · V = 0

Which can be written in terms of concentration:

CA = CA0 - ((-rA · V) / FA0)

The model solves this algebraic equation for the outlet concentration.

---

## CSTR Train

A series of CSTRs can approximate plug flow behavior.

Each reactor uses the outlet concentration from the previous reactor as its inlet concentration:

CAₙ₊₁ = CSTR(CAₙ)

As the number of tanks increases, the system approaches PFR performance.

---

# Levenspiel Diagram

The project also generates a **Levenspiel plot**, a classic reactor design visualization:

F_A0 / (-r_A) vs conversion X

This diagram is used to compare reactor performance:

• Area under the curve → required PFR volume  
• Rectangle area → required CSTR volume  

The simulation illustrates how reactor type affects required reactor volume for a given conversion.

---

# Example Plots

The simulation produces the following engineering plots:

• Concentration vs reactor volume  
• Conversion vs reactor volume  
• Levenspiel diagram  
• Comparison between PFR, CSTR, and CSTR train behavior

Example outputs are included in the `example_plots/` folder.

---

# Project Structure

```
chemical-reactor-simulation-tool
│
├── main.py
├── reactor_model.py
├── plotting.py
├── parameters.py
├── requirements.txt
├── README.md
│
└── example_plots/
    ├── concentration_plot.png
    ├── conversion_plot.png
    └── levenspiel_plot.png
```

---

# Installation

### Clone the repository

```
git clone https://github.com/MatthewNguyen865/chemical-reactor-simulation-tool.git
```

### Install dependencies

```
pip install -r requirements.txt
```

### Run the simulation

```
python main.py
```

---

# Technologies Used

• Python  
• NumPy  
• SciPy  
• Matplotlib  

---

# Skills Demonstrated

## Chemical Engineering

• Reactor design equations  
• Reaction kinetics modeling  
• Levenspiel analysis  
• Comparison of ideal reactor types  

## Programming

• Scientific computing in Python  
• Numerical solution of differential equations  
• Data visualization  
• Modular project structure

---

# Future Improvements

Potential extensions for the simulator:

• Higher-order and multiple reaction systems  
• Temperature-dependent kinetics (Arrhenius equation)  
• Non-isothermal reactor modeling (energy balances)  
• Optimization of reactor volume for target conversion  
• Interactive visualization or GUI interface

---

# Author

Matthew Nguyen  
Chemical Engineering Student  
Texas A&M University