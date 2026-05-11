# Plug Flow Reactor Simulator

This project simulates a simple plug flow reactor (PFR) using Python.

The purpose of this project was to learn how chemical engineering
reactor models can be implemented computationally.

---

## Reaction

A → B

The reaction follows first order kinetics:

rA = -kCA

where:

rA = reaction rate of species A  
k = reaction rate constant  
CA = concentration of A  

---

## Reactor Model

For a plug flow reactor, the concentration changes along reactor volume:

dCA/dV = rA / FA0

This differential equation is solved numerically using scipy.

---

## What This Project Demonstrates

- translating chemical engineering equations into code
- numerical solution of differential equations
- data visualization using matplotlib
- modular Python programming

---

## Running the Simulation

Install dependencies:

pip install -r requirements.txt

Run the model:

python main.py

---

## Future Improvements

Possible upgrades to this project:

- temperature dependent reaction kinetics
- multiple reactions
- energy balance in the reactor
- graphical user interface