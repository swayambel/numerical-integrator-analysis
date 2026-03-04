import numpy as np

def simulate(step_function, derivatives, dt, steps, energy_func):
    state = np.array([1.0, 0.0, 0.0, 1.0])

    trajectory = []
    energy = []

    for _ in range(steps):
        trajectory.append(state[:2])
        energy.append(energy_func(state))
        state = step_function(state, dt, derivatives)

    return np.array(trajectory), np.array(energy)
