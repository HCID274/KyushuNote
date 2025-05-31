# task7.py
# Assignment 7: Predator-Prey Model with Modified Parameters

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as desol

# --- Parameters Chosen for this Assignment ---
# These values are different from the lecture examples to produce a unique diagram.

# Coefficients for the Lotka-Volterra equations:
# a: prey growth rate
# b: predation rate (effect of predator on prey)
# c: predator growth rate from eating prey
# d: predator death rate
a_new = 0.8  # Original example was 1.0 or 2.0. Let's make prey grow a bit slower.
b_new = 0.08 # Original example was 1.0. Let's make predation less impactful per encounter,
             # or encounters less frequent.
c_new = 0.03 # Original example was 1.0. Let's make predators less efficient at converting prey to offspring.
d_new = 0.6  # Original example was 1.0. Let's increase predator natural death rate.

# Initial populations:
# f0_new[0]: initial prey population (x)
# f0_new[1]: initial predator population (y)
f0_new = [50.0, 5.0] # Original example was [1.0, 0.1] or similar.
                     # Let's start with significantly more prey and a moderate number of predators.

# --- End of Chosen Parameters ---


# Define the right-hand side of the differential equation system (Lotka-Volterra model)
def predator_prey(f, t, a, b, c, d):
    """
    Returns the rate of change for prey and predator populations.

    Model equations:
        dx/dt = ax - bxy  (prey)
        dy/dt = cxy - dy  (predator)

    Parameters:
    f (list/array): Current populations [prey, predator] -> [f[0], f[1]]
    t (float): Current time (independent variable, not explicitly used in this autonomous system)
    a, b, c, d (float): Model coefficients
    """
    prey_population = f[0]
    predator_population = f[1]

    d_prey_dt = a * prey_population - b * prey_population * predator_population
    d_predator_dt = c * prey_population * predator_population - d * predator_population

    return [d_prey_dt, d_predator_dt]

# Time points for the simulation
nt = 2000       # Number of time points
tmax = 100.0    # Maximum time for simulation (increased to see more cycles if they appear)
t = np.linspace(0, tmax, nt) # Array of time points from 0 to tmax

# Solve the differential equations using the chosen parameters
# `desol.odeint` integrates the system of ordinary differential equations.
# - `predator_prey`: The function defining the derivatives.
# - `f0_new`: The initial conditions for [prey, predator].
# - `t`: The time points at which to solve.
# - `args`: Extra arguments to pass to the `predator_prey` function (our coefficients).
solution = desol.odeint(predator_prey, f0_new, t, args=(a_new, b_new, c_new, d_new))

# Extract prey and predator populations from the solution
# solution[:, 0] contains all prey populations at each time point
# solution[:, 1] contains all predator populations at each time point
prey_over_time = solution[:, 0]
predator_over_time = solution[:, 1]

# --- Plotting the results ---
fig = plt.figure(figsize=(10, 6)) # Create a figure for the plot
ax = fig.add_axes([0.15, 0.1, 0.8, 0.8]) # Add axes to the figure [left, bottom, width, height]

# Plot prey population over time
ax.plot(t, prey_over_time, color='red', linestyle='-', label=r"$x$: Prey Population")
# Plot predator population over time
ax.plot(t, predator_over_time, color='blue', linestyle='--', label=r"$y$: Predator Population")

# Add labels and title
ax.set_xlabel("Time")
ax.set_ylabel("Population Size")
ax.set_title(f"Predator-Prey Dynamics\n(a={a_new}, b={b_new}, c={c_new}, d={d_new}; x0={f0_new[0]}, y0={f0_new[1]})")
ax.legend() # Show the legend
ax.grid(True, linestyle=':', alpha=0.7) # Add a light grid for readability

# Display the plot
plt.show()

# Print the chosen parameters to the console as well, for easy reference
print("--- Assignment 7: Chosen Parameters ---")
print(f"Initial prey population (x0): {f0_new[0]}")
print(f"Initial predator population (y0): {f0_new[1]}")
print(f"Prey growth rate (a): {a_new}")
print(f"Predation rate (b): {b_new}")
print(f"Predator efficiency (c): {c_new}")
print(f"Predator death rate (d): {d_new}")
print("---------------------------------------")