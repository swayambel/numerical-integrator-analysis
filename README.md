# Numerical Integrator Stability Analysis

## Overview

This project investigates the numerical stability and energy conservation behavior of different time-integration methods applied to the two-body gravitational problem. The objective is to understand how numerical errors accumulate over long simulations and how different integrators handle conserved physical quantities.

The study compares three commonly used numerical methods:

* Euler Method
* Runge-Kutta 2 (RK2)
* Runge-Kutta 4 (RK4)

The analysis focuses on how these methods affect orbital stability, radius drift, and total mechanical energy conservation.

---

## Physical Model

The system being simulated is a classical two-body gravitational problem. The motion is governed by Newton's law of gravitation:

d²r/dt² = -GM r / |r|³

where:

* G is the gravitational constant
* M is the central mass
* r is the position vector

For simplicity, the gravitational parameter is normalized:

GM = 1

Initial conditions correspond to a circular orbit:

Position: (1, 0)
Velocity: (0, 1)

---

## Numerical Methods Studied

### Euler Method

A first-order integrator that estimates the next state using the current derivative. It is simple but introduces large numerical errors over long simulations.

### RK2 (Second-Order Runge-Kutta)

Improves accuracy by sampling the derivative at two points and averaging the result.

### RK4 (Fourth-Order Runge-Kutta)

A higher-order integrator that evaluates the derivative four times per timestep, significantly reducing truncation error.

---

## Analysis Performed

The project evaluates the behavior of each integrator using several diagnostics:

### Orbit Geometry

The trajectory of the orbit is plotted to visually inspect stability and long-term behavior.

### Radius Drift

The radius of the orbit is tracked over time to detect gradual expansion or contraction.

### Energy Drift

Specific mechanical energy is monitored to determine how well each integrator preserves energy conservation.

---

## Key Observations

Typical behavior observed:

* Euler method quickly causes the orbit to spiral outward due to energy gain.
* RK2 reduces the error but still introduces noticeable long-term drift.
* RK4 maintains orbital stability significantly longer with much smaller energy deviation.

These results demonstrate how integrator order influences long-term numerical stability.

---

## Tools Used

Python
NumPy
Matplotlib
Google Colab for experimentation and visualization

---

## Purpose of the Project

This project is intended as a computational physics study of numerical integrators and their impact on long-term orbital simulations. It demonstrates how algorithmic choices influence numerical stability when modeling dynamical systems.

---

## Future Work

Possible extensions include:

* Implementing symplectic integrators such as Velocity Verlet
* Comparing angular momentum conservation
* Performing timestep sensitivity analysis
* Evaluating long-term stability across different timestep sizes

---

## License

This project is released under the MIT License.
