import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams["font.family"] = "Roboto Condensed"

# Ensure the output directory exists
os.makedirs("input/svg", exist_ok=True)

# --- Value Function ---
def value_function(x, alpha=0.5, lambda_=2.25):
    """Prospect Theory Value Function.
    Args:
        x: Array of values (gains or losses).
        alpha: Concavity/convexity parameter (default: 0.5).
        lambda_: Loss aversion parameter (default: 2.25).
    Returns:
        v(x): Value function output.
    """
    return np.where(x >= 0, x ** alpha, -lambda_ * (np.abs(x)) ** alpha)

# Generate x values (symmetric around 0)
XLIM = 5
x = np.linspace(-XLIM, XLIM, 500)
v = value_function(x)

# Plot value function
plt.figure(figsize=(6, 6))
plt.plot(x, v, color="black", linewidth=2, label="Value Function (v(x))")
plt.plot(x, x, color="black", linestyle="--", linewidth=1, label="Linear (y = x)")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.xlabel("Outcome (x)", fontsize=12)
plt.ylabel("Value (v(x))", fontsize=12)
plt.title("Prospect Theory: Value Function", fontsize=14)
plt.grid(False)
plt.xlim(-XLIM - 0.5, XLIM + 0.5)
plt.ylim(-XLIM - 0.5, XLIM + 0.5)
plt.legend(fontsize=10)
plt.tight_layout()

# Save as SVG
plt.savefig("../input/svg/value-function.svg", format="svg", dpi=300, facecolor="white", edgecolor="none")
plt.close()

# --- Probability-Weighting Function ---
def probability_weighting(p, gamma=0.61):
    """Prospect Theory Probability-Weighting Function.
    Args:
        p: Array of probabilities (0 to 1).
        gamma: Curvature parameter (default: 0.61).
    Returns:
        w(p): Weighted probability.
    """
    return p ** gamma / (p ** gamma + (1 - p) ** gamma) ** (1 / gamma)

# Generate probability values
p = np.linspace(0, 1, 500)
w = probability_weighting(p)

# Plot probability-weighting function
plt.figure(figsize=(6, 6))
plt.plot(p, w, color="black", linewidth=2, label="Probability-Weighting (w(p))")
plt.plot(p, p, color="black", linestyle="--", linewidth=1, label="Linear (w(p) = p)")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.xlabel("Probability (p)", fontsize=12)
plt.ylabel("Weighted Probability (w(p))", fontsize=12)
plt.title("Prospect Theory: Probability-Weighting Function", fontsize=14)
plt.grid(False)
plt.xlim(-0.05, 1.05)
plt.ylim(-0.05, 1.05)
plt.legend(fontsize=10)
plt.tight_layout()

# Save as SVG
plt.savefig("../input/svg/probability-function.svg", format="svg", dpi=300, facecolor="white", edgecolor="none")
plt.close()

print("Figures saved to input/svg/value-function.svg and input/svg/probability-function.svg")