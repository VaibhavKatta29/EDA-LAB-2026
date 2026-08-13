import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the ID-VGS data
df = pd.read_csv("MOSFET_ID_VGS.csv")

# Select the VDS = 5 V data
data = df[df["V_DS (V)"] == 5.0].sort_values("V_GS (V)")

vgs = data["V_GS (V)"].to_numpy()
id_current = data["I_D (mA)"].to_numpy()

# Calculate sqrt(ID)
sqrt_id = np.sqrt(id_current)

# Select the linear region
linear_region = vgs >= 2.0

# Linear fit: sqrt(ID) = m*VGS + b
m, b = np.polyfit(vgs[linear_region], sqrt_id[linear_region], 1)

# Find threshold voltage from x-intercept
Vt = -b / m

# Calculate the fitted line
sqrt_id_fit = m * vgs + b

# Plot the data and linear extrapolation
plt.figure(figsize=(8, 6))

plt.plot(vgs, sqrt_id, "o-", label="Data")
plt.plot(vgs, sqrt_id_fit, "--", label="Linear fit")

# Mark the threshold voltage
plt.axvline(Vt, linestyle="--", label=f"V_T = {Vt:.2f} V")

plt.xlabel("$V_{GS}$ (V)")
plt.ylabel(r"$\sqrt{I_D}$ ($\sqrt{\mathrm{mA}}$)")
plt.title(r"Threshold Voltage Extraction")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

print("Threshold Voltage V_T =", Vt, "V")

# Plot sqrt(ID) versus VGS
plt.figure(figsize=(8, 6))
plt.plot(vgs, sqrt_id, "o-", label="Data")

plt.xlabel("$V_{GS}$ (V)")
plt.ylabel(r"$\sqrt{I_D}$ ($\sqrt{\mathrm{mA}}$)")
plt.title(r"Threshold Voltage Extraction: $\sqrt{I_D}$ vs $V_{GS}$")
plt.grid(True)

plt.legend()
plt.tight_layout()
plt.show()

# Plot ID versus VGS
plt.figure(figsize=(8, 6))

plt.plot(vgs, id_current, "o-")

plt.xlabel("$V_{GS}$ (V)")
plt.ylabel("$I_D$ (mA)")
plt.title("$I_D$ vs $V_{GS}$")
plt.grid(True)

plt.tight_layout()
plt.show()