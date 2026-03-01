import matplotlib.pyplot as plt

from physics import derivatives, specific_energy
from integrators import euler_step, rk2_step, rk4_step
from analysis import simulate

dt = 0.01
steps = 5000

traj_euler, energy_euler = simulate(euler_step, derivatives, dt, steps, specific_energy)
traj_rk2, energy_rk2 = simulate(rk2_step, derivatives, dt, steps, specific_energy)
traj_rk4, energy_rk4 = simulate(rk4_step, derivatives, dt, steps, specific_energy)

delta_euler = energy_euler - energy_euler[0]
delta_rk2 = energy_rk2 - energy_rk2[0]
delta_rk4 = energy_rk4 - energy_rk4[0]

plt.plot(traj_euler[:,0], traj_euler[:,1], label="Euler")
plt.plot(traj_rk2[:,0], traj_rk2[:,1], label="RK2")
plt.plot(traj_rk4[:,0], traj_rk4[:,1], label="RK4")

plt.gca().set_aspect('equal')
plt.legend()
plt.title("Integrator Comparison")
plt.show()

plt.plot(energy_euler, label="Euler")
plt.plot(energy_rk2, label="RK2")
plt.plot(energy_rk4, label="RK4")

plt.legend()
plt.title("Specific Energy vs Time")
plt.show()



