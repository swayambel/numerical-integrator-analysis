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

plt.plot(trajectory[:,0], trajectory[:,1], label="Euler Orbit")
plt.scatter(trajectory[0,0], trajectory[0,1], color='green', label="Start")
plt.scatter(trajectory[-1,0], trajectory[-1,1], color='red', label="End")

plt.gca().set_aspect('equal')
plt.legend()
plt.title("Orbit using Euler Method")
plt.show()


# RK4 Integrator
def rk4_steps(state,dt):
  k1 = derivatives(state)
  k2 = derivatives(state + 0.5 * dt * k1)
  k3 = derivatives(state + 0.5 * dt * k2)
  k4 = derivatives(state + dt * k3)
  return state + (dt/6.0) * (k1 + 2*k2 + 2*k3 + k4)

state = np.array([1.0, 0.0, 0.0, 1.0])

trajectory_rk4 = []
for _ in range(steps):
    trajectory_rk4.append(state[:2])
    state = rk4_steps(state,dt)
trajectory_rk4 = np.array(trajectory_rk4)

plt.gca().set_aspect('equal')
plt.plot(trajectory_rk4[:,0], trajectory_rk4[:,1], label = "RK4 Orbit")
plt.scatter(trajectory_rk4[0,0], trajectory_rk4[0,1], color='green', label='Start')
plt.scatter(trajectory_rk4[0,0], trajectory_rk4[0,1], color='red', label='End')
