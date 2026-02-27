import numpy as np

GM = 1.0

def derivatives(state):
    x, y, vx, vy = state
    r = np.sqrt(x**2 + y**2)
    ax = -GM * x / r**3
    ay = -GM * y / r**3
    return np.array([vx, vy, ax, ay])

def specific_energy(state):
    x, y, vx, vy = state
    r = np.sqrt(x**2 + y**2)
    v2 = vx**2 + vy**2
    return 0.5 * v2 - GM / r

def radius(state):
    x, y, _, _ = state
    return np.sqrt(x**2 + y**2)
