import numpy as np
import matplotlib.pyplot as plt

# Parameters
final_time = 5.0
Nx = 200
Nt = 200  # Number of time steps
v = -1.0  # Speed of advection
x_min, x_max = -5, 5

# Spatial and time grids
delta_x = (x_max - x_min) / Nx
delta_t = final_time / Nt
x = np.linspace(x_min, x_max, Nx)
t = np.linspace(0, final_time, Nt)

# Initial condition: Gaussian
def initial_condition(x):
    return np.exp(-((x - 2.5) / 0.5) ** 2)

# Analytical solution
def analytical_solution(x, t, v):
    return np.exp(-((x - 2.5 - v * t) / 0.5) ** 2)

# Create a 2D array to hold the solution at all time steps
solution_2d = np.zeros((Nt, Nx))

# Fill the solution array with the analytical solution at each time step
for j in range(Nt):
    solution_2d[j, :] = analytical_solution(x, t[j], v)

# Plot the 2D analytical solution
fig, ax = plt.subplots(figsize=(8, 6))
plt.pcolormesh(x, t, solution_2d, cmap='viridis', shading='auto')
plt.colorbar(label='$u(x, t)$')
plt.grid(color='r', linestyle='--')

plt.xlabel('x')
plt.ylabel('t')
plt.title('Analytical Solution of Advection Equation')
plt.show()
