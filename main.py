# Numerical Integrator Analysis
import numpy as np

# Gravitational parameter (GM)
GM = 1.0 

def derivatives(state):
    x, y, vx, vy = state
    
    r = np.sqrt(x**2 + y**2)
    
    ax = -GM * x / r**3
    ay = -GM * y / r**3
    
    return np.array([vx, vy, ax, ay])
  
# Test state: circular orbit initial guess
state = np.array([1.0, 0.0, 0.0, 1.0])

print("Derivatives:", derivatives(state))

def euler_step(state, dt):
    return state + dt * derivatives(state)

dt = 0.01
steps = 5000

state = np.array([1.0, 0.0, 0.0, 1.0])

trajectory = []

for _ in range(steps):
    trajectory.append(state[:2])  
    state = euler_step(state, dt)

trajectory = np.array(trajectory)

import matplotlib.pyplot as plt

plt.plot(trajectory[:,0], trajectory[:,1], label="Orbit")
plt.scatter(trajectory[0,0], trajectory[0,1], color='green', label="Start")
plt.scatter(trajectory[-1,0], trajectory[-1,1], color='red', label="End")

plt.gca().set_aspect('equal')
plt.legend()
plt.title("Orbit using Euler Method")
plt.show()
