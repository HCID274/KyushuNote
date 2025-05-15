import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import os

# --- Config ---
data_filename = os.path.join(os.path.dirname(__file__), "kadai5.dat")
output_plot_original = "task5_fit_original_scale.png"
output_plot_linearized = "task5_fit_linearized_scale.png"
output_plot_semilogy = "task5_fit_semilogy_scale.png"

# --- Load Data ---
try:
    data = np.loadtxt(data_filename, delimiter=',', skiprows=1)
    x_data = data[:, 0]
    y_data = data[:, 1]
except FileNotFoundError:
    print(f"Error: File '{data_filename}' not found.")
    exit()
except Exception as e:
    print(f"Error reading file: {e}")
    exit()

if len(x_data) == 0:
    print("Error: No data loaded.")
    exit()

# --- Linearize: ln(y) = ln(a) + bx ---
try:
    y_prime_data = np.log(y_data)
except RuntimeWarning as w:
    print(f"Warning during log(): {w}")
    print("Check for zero or negative values in y_data.")

# --- Linear Regression (OLS) ---
X_sm = sm.add_constant(x_data)
model = sm.OLS(y_prime_data, X_sm)
result = model.fit()

a_prime = result.params[0]
b = result.params[1]
sigma_a_prime = result.bse[0]
sigma_b = result.bse[1]
R_squared = result.rsquared

# --- Recover a from ln(a) ---
a = np.exp(a_prime)
sigma_a = a * sigma_a_prime

# --- Output ---
print("\n--- Fitted Model: y = a * exp(bx) ---")
print(f"ln(a): {a_prime:.6f} ± {sigma_a_prime:.6f}")
print(f"a    : {a:.6f} ± {sigma_a:.6f}")
print(f"b    : {b:.6f} ± {sigma_b:.6f}")
print(f"R²   : {R_squared:.6f}")

print("\n--- Statsmodels Summary (ln(y) vs x) ---")
print(result.summary())

print("\n--- Final Result ---")
print(f"a = {a:.4f} ± {sigma_a:.4f}")
print(f"b = {b:.4f} ± {sigma_b:.4f}")
print(f"R² = {R_squared:.4f}")

# --- Plot: Original Scale ---
plt.figure(figsize=(10, 6))
plt.plot(x_data, y_data, 'x', label="Data")
x_fit = np.linspace(min(x_data), max(x_data), 200)
y_fit = a * np.exp(b * x_fit)
plt.plot(x_fit, y_fit, 'r', label=f"Fit: y = {a:.3f}exp({b:.3f}x)")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Fit: y = a * exp(bx)")
plt.legend()
plt.grid(True)
plt.savefig(output_plot_original)
print(f"Saved: {output_plot_original}")

# --- Plot: Linearized (ln(y)) ---
plt.figure(figsize=(10, 6))
plt.plot(x_data, y_prime_data, 'o', label="ln(y)")
y_prime_fit = a_prime + b * x_fit
plt.plot(x_fit, y_prime_fit, 'g', label=f"Fit: ln(y) = {a_prime:.3f} + {b:.3f}x")
plt.xlabel("x")
plt.ylabel("ln(y)")
plt.title("Linear Fit: ln(y) = ln(a) + bx")
plt.legend()
plt.grid(True)
plt.savefig(output_plot_linearized)
print(f"Saved: {output_plot_linearized}")

# --- Plot: Semilogy ---
plt.figure(figsize=(10, 6))
plt.semilogy(x_data, y_data, 'x', label="Data")
plt.semilogy(x_fit, y_fit, 'r', label=f"Fit: y = {a:.3f}exp({b:.3f}x)")
plt.xlabel("x")
plt.ylabel("y (log scale)")
plt.title("Fit on Semilog Scale")
plt.legend()
plt.grid(True, which="both", ls="-")
plt.savefig(output_plot_semilogy)
print(f"Saved: {output_plot_semilogy}")

plt.show()
