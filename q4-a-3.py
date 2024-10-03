import numpy as np
import matplotlib.pyplot as plt

# Parameters
final_time = 5.0
Nx = 200
CFL = np.array([0.01, 0.1, 0.5])
v = -1.0  # Speed of advection

# Initial condition: Gaussian
def initial_condition(x):
    return np.exp(-((x - 2.5) / 0.5) ** 2)

# Analytical solution for comparison
def analytical_solution(x, t, v):
    return np.exp(-((x - 2.5 - v * t) / 0.5) ** 2)

# Function to calculate the error
def calculate_error(numerical_solution, x, t, v):
    Nt, Nx = numerical_solution.shape
    error = np.zeros_like(numerical_solution)
    for j in range(Nt):
        u_exact = analytical_solution(x, t[j], v)
        error[j, :] = np.abs(u_exact - numerical_solution[j, :])
    return error

# Loop over each CFL condition
for i in range(len(CFL)):
    delta_x = 10 / Nx
    delta_t = CFL[i] * delta_x

    x = np.arange(delta_x / 2.0 - 5, 5, delta_x)
    Nt = int(np.ceil(final_time / delta_t)) + 2
    t = np.zeros(Nt)
    t[0] = 0.0

    solution = np.zeros((Nt, Nx))
    solution[0, :] = initial_condition(x)

    curr_time = t[0]
    u = solution[0, :]

    output_number = 0
    while curr_time < final_time:
        # Compute the RHS of the ODE (first-order upwind scheme)
        dudt = (np.roll(u, -1) - np.roll(u, 1)) / (2 * delta_x)

        # Update numerical solution
        u = u + delta_t * dudt

        # Increase time by delta t
        curr_time = curr_time + delta_t

        # Store the new values in our array
        output_number += 1
        solution[output_number, :] = u
        t[output_number] = curr_time

    # Trim the unused part of the solution array
    t = t[:output_number]
    solution = solution[:output_number, :]

    # Calculate the error using the analytical solution
    error = calculate_error(solution, x, t, v)

    # Plot the error
    fig, ax = plt.subplots(figsize=(7, 5))
    plt.pcolormesh(x, t, error, cmap='inferno', shading='auto')
    plt.colorbar(label='Error')
    plt.grid(color='r', linestyle='--')

    plt.xlabel('x')
    plt.ylabel('t')
    plt.title(f'Error in Advection Solution\nCFL = {CFL[i]:g}, Delta x = {delta_x:g}, Delta t = {delta_t:g}')
    plt.show()
