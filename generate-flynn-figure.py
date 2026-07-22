import numpy as np
import matplotlib.pyplot as plt
import os

plt.rcParams["font.family"] = "Roboto Condensed"

# Ensure the output directory exists
os.makedirs("input/svg", exist_ok=True)

# ============================================================
# Panel A: Yearly mean IQ from fitted line (birth cohort, 1962–1992)
# ============================================================
panel_a_years = np.array([
    1962, 1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971,
    1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980, 1981,
    1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990, 1991,
    1992
])
panel_a_iq = np.array([
    99.5, 99.4, 99.6, 100.1, 100.7, 101.0, 101.1, 101.4, 101.6, 102.0,
    102.3, 102.4, 102.5, 102.3, 102.0, 101.8, 101.6, 101.3, 101.0, 101.2,
    101.4, 101.1, 100.9, 101.3, 100.8, 100.2,  99.9,  99.4,  99.3,  99.6,
    99.9
])

# ============================================================
# Create figure
# ============================================================
fig, ax = plt.subplots(figsize=(6, 5))
ax.set_title("The Flynn effect and its reversal (Bratsberg & Rogeberg, 2018)", fontsize=14)
ax.plot(panel_a_years, panel_a_iq, color="black", linewidth=2.5)
ax.set_xlabel("Birth year", fontsize=12)
ax.set_ylabel("IQ score", fontsize=12)
ax.set_xlim(1960, 1994)
ax.set_ylim(98.5, 103.5)
ax.axhline(100, color="gray", linewidth=0.5, linestyle="--")
ax.grid(False)

plt.tight_layout()
plt.savefig("input/svg/flynn-effect.svg", format="svg", dpi=300,
            facecolor="white", edgecolor="none")
plt.close()

print("Figure saved to input/svg/flynn-effect.svg")