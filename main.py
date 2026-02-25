# Numerical Integrator Analysis
import numpy as np

# Gravitational parameter (GM)
GM = 1.0  # Using normalized units

def derivatives(state):
    x, y, vx, vy = state
    
    r = np.sqrt(x**2 + y**2)
    
    ax = -GM * x / r**3
    ay = -GM * y / r**3
    
    return np.array([vx, vy, ax, ay])
  
# Test state: circular orbit initial guess
state = np.array([1.0, 0.0, 0.0, 1.0])

print("Derivatives:", derivatives(state))

import matplotlib.pyplot as plt

plt.plot(trajectory[:,0], trajectory[:,1])
plt.gca().set_aspect('equal')
plt.title("Orbit using Euler Method")
plt.show()
