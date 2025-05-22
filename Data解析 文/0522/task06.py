import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import os

os.chdir(os.path.dirname(__file__))

# --- Config ---
FILENAME = "kadai6.dat"
MAX_ORDER = 9

# --- 1. Load data ---
if not os.path.exists(FILENAME):
    print(f"Error: '{FILENAME}' not found in current directory.")
    exit()

try:
    data = pd.read_csv(FILENAME, comment='#', sep=',', names=['x', 'y'])
    data['x'] = pd.to_numeric(data['x'], errors='coerce')
    data['y'] = pd.to_numeric(data['y'], errors='coerce')
    if data.isnull().any().any():
        print("Warning: Invalid numeric values found. Dropping NaNs.")
        data.dropna(inplace=True)
        data.reset_index(drop=True, inplace=True)
    if data.empty:
        print("Error: No valid data after cleanup.")
        exit()
    x_data, y_data = data['x'], data['y']
    print(f"Loaded {len(data)} data points from '{FILENAME}'.")
except Exception as e:
    print(f"Critical error reading file: {e}")
    import traceback
    traceback.print_exc()
    exit()

# --- 2. Fit polynomial models ---
orders = list(range(1, MAX_ORDER + 1))
r2_vals, aic_vals, bic_vals = [], [], []
models = {}

print("\nFitting polynomial models...")
for order in orders:
    if len(x_data) < order + 1:
        print(f"Insufficient data for order {order}. Skipping.")
        r2_vals.append(np.nan)
        aic_vals.append(np.nan)
        bic_vals.append(np.nan)
        models[order] = None
        continue
    try:
        terms = [f"I(x**{i})" for i in range(1, order + 1)]
        formula = "y ~ " + " + ".join(terms)
        model = smf.ols(formula, data=pd.DataFrame({'x': x_data, 'y': y_data}))
        result = model.fit()
        r2_vals.append(result.rsquared)
        aic_vals.append(result.aic)
        bic_vals.append(result.bic)
        models[order] = result
    except Exception as e:
        print(f"Error fitting order {order}: {e}")
        r2_vals.append(np.nan)
        aic_vals.append(np.nan)
        bic_vals.append(np.nan)
        models[order] = None

# --- 3. Select best model by AIC ---
if not all(np.isnan(aic_vals)):
    valid_idxs = [i for i, v in enumerate(aic_vals) if not np.isnan(v)]
    best_aic_idx = valid_idxs[np.argmin(np.array(aic_vals)[valid_idxs])]
    best_order_aic = orders[best_aic_idx]
    best_model_aic = models[best_order_aic]
    print(f"\n--- Best fit by AIC: Order {best_order_aic} ---")
    if best_model_aic:
        print("Coefficients:\n", best_model_aic.params)
        print("Standard Errors:\n", best_model_aic.bse)
        print(f"R²: {best_model_aic.rsquared:.4f}, AIC: {best_model_aic.aic:.2f}, BIC: {best_model_aic.bic:.2f}")
    valid_bic_idxs = [i for i, v in enumerate(bic_vals) if not np.isnan(v)]
    best_bic_idx = valid_bic_idxs[np.argmin(np.array(bic_vals)[valid_bic_idxs])]
    best_order_bic = orders[best_bic_idx]
    if models.get(best_order_bic):
        print(f"\n--- Best fit by BIC: Order {best_order_bic} ---")
        print(f"(AIC={models[best_order_bic].aic:.2f}, BIC={models[best_order_bic].bic:.2f})")
else:
    print("Failed to determine best order (AICs are all NaN).")
    best_order_aic = orders[0]
    best_model_aic = None

# --- 4. Plotting ---
plt.style.use('seaborn-v0_8-whitegrid')
try:
    plt.rcParams['font.sans-serif'] = ['Arial', 'sans-serif']
    plt.rcParams['axes.unicode_minus'] = False
except Exception as e:
    print(f"Font setup error: {e}")

fig = plt.figure(figsize=(12, 8))

# Plot 1: Data and best fit
ax1 = plt.subplot2grid((2, 2), (0, 0), rowspan=2)
if not x_data.empty and not y_data.empty:
    ax1.scatter(x_data, y_data, marker='x', label='Data', color='steelblue', s=30, alpha=0.7)
    if best_model_aic:
        x_plot = np.linspace(x_data.min(), x_data.max(), 200)
        y_plot = best_model_aic.predict(pd.DataFrame({'x': x_plot}))
        ax1.plot(x_plot, y_plot, color='red', linewidth=2,
                 label=f'Best fit (Order {best_order_aic})')
        ax1.set_title(f'Best Polynomial Fit (Order {best_order_aic})')
    else:
        ax1.set_title('Data (No fit)')
else:
    ax1.set_title('No data to plot')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.legend()
ax1.grid(True, linestyle='--', alpha=0.7)

# Plot 2: R-squared
ax2 = plt.subplot2grid((2, 2), (0, 1))
ax2.plot(orders, r2_vals, marker='x', linestyle='-', color='forestgreen')
if 'best_aic_idx' in locals() and not np.isnan(r2_vals[best_aic_idx]):
    ax2.scatter(best_order_aic, r2_vals[best_aic_idx], color='red', s=100, zorder=5, label=f'Best (Order {best_order_aic})')
    ax2.legend(fontsize='small')
ax2.set_xlabel('Order')
ax2.set_ylabel('R-squared')
ax2.set_title('R-squared')
ax2.set_xticks(orders)
ax2.grid(True, linestyle='--', alpha=0.5)

# Plot 3: AIC / BIC
ax3 = plt.subplot2grid((2, 2), (1, 1))
ax3.plot(orders, aic_vals, marker='o', linestyle='-', color='darkorange', label='AIC')
ax3.plot(orders, bic_vals, marker='s', linestyle='--', color='purple', label='BIC', alpha=0.7)
handles = ax3.get_legend_handles_labels()[0]
from matplotlib.lines import Line2D
if not np.isnan(aic_vals[best_aic_idx]):
    handles.append(Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10, label=f'Min AIC (Order {best_order_aic})'))
if best_order_aic != best_order_bic and not np.isnan(bic_vals[best_bic_idx]):
    handles.append(Line2D([0], [0], marker='D', color='w', markerfacecolor='magenta', markersize=10, label=f'Min BIC (Order {best_order_bic})'))
ax3.legend(handles=handles, fontsize='small')
ax3.set_xlabel('Order')
ax3.set_ylabel('Criterion Value')
ax3.set_title('AIC / BIC')
ax3.set_xticks(orders)
ax3.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout(pad=2.0)
plt.suptitle("Polynomial Regression Analysis", fontsize=16, y=0.99)
fig.subplots_adjust(top=0.92)
plt.show()

print("\nDone.")
