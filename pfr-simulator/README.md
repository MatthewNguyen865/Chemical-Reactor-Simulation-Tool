# Plug Flow Reactor (PFR) Simulator

A Python-based numerical simulation of a Plug Flow Reactor (PFR) for modeling concentration profiles and conversion in a first-order chemical reaction system.

This project demonstrates how core chemical reaction engineering principles can be implemented using numerical methods and scientific computing in Python.

---

# Overview

This simulator models a **Plug Flow Reactor (PFR)**, an ideal reactor type commonly used in chemical engineering where fluid flows through a tubular system with no axial mixing.

The model computes how reactant concentration changes along reactor volume by solving the governing differential equations numerically.

---

# Governing Reaction

A → B

First-order reaction kinetics:

rA = -k * CA

Where:

- rA = rate of reaction (mol/L·s)  
- k = rate constant (1/s)  
- CA = concentration of species A (mol/L)

---

# Reactor Model

The system is based on the PFR design equation:

dFA / dV = rA

For constant volumetric flow rate:

dCA / dV = rA / v0

Where:

- V = reactor volume (L)  
- v0 = volumetric flow rate (L/s)  
- CA = concentration of A (mol/L)

This equation is solved numerically using discretization of the reactor volume.

---

# Numerical Method

The reactor is divided into small finite volume steps.

At each step:
1. Reaction rate is calculated using current concentration
2. Concentration is updated using a numerical integration method
3. The solution advances along the reactor volume

This approach approximates the continuous differential equation using a stepwise numerical solver (Euler-type integration).

---

# Key Features

- Simulates concentration profiles along reactor volume
- Implements first-order reaction kinetics
- Numerically solves the PFR design equation
- Computes reactant conversion
- Generates engineering plots of reactor behavior

---

# Model Inputs

The simulation accepts the following parameters:

- Initial concentration (CA0)
- Reaction rate constant (k)
- Volumetric flow rate (v0)
- Total reactor volume (V)
- Number of discretization steps

---

# Outputs

The model generates:

- Concentration vs reactor volume profile
- Outlet concentration
- Reactant conversion:

X = (CA0 - CA) / CA0

---

# Engineering Applications

This simulation demonstrates:

- Numerical solution of chemical reaction engineering models
- Relationship between kinetics and reactor performance
- Behavior of ideal plug flow reactors under first-order kinetics
- Discretization of differential design equations

---

# Project Structure

pfr-simulator/
|
|--- main.py
|--- parameters.py
|--- plots.py
|--- README.md
|--- requirements.txt

---

# Installation

### Clone the repository:

git clone https://github.com/MatthewNguyen865/pfr-simulator.git

### Install required packages:

pip install r- requirements.txt

### Run the program:

python main.py

---

# Usage

Run the simulation:

python main.py

---

# Skills Demonstrated

- Chemical reaction engineering fundamentals
- Numerical methods for differential equations
- Scientific programming in Python
- Data visualization (matplotlib)
- Modular code organization

---

# Future Improvements

Planned extensions:

- Second-order and multi-reaction systems
- Temperature-dependent kinetics (Arrhenius model)
- Non-isothermal reactor modeling (energy balance)
- Comparison between PFR and CSTR performance
- Interactive or GUI-based simulation interface

---

#Author

Matthew Nguyen
Chemical Engineering Student
Texas A&M University