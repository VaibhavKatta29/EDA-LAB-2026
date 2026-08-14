import pandas as pd
import matplotlib.pyplot as plt

# Load the diode data
df = pd.read_csv("Diode_IV_Temperature.csv")

# Plot I-V curve for each temperature
plt.figure(figsize=(10, 6))

for temperature, group in df.groupby("T (C)"):
    group = group.sort_values("V (V)")

    plt.plot(
        group["V (V)"],
        group["I (mA)"],
        marker="o",
        linewidth=2,
        label=f"T = {temperature} °C"
    )

plt.title("Diode I-V Characteristics at Different Temperatures")
plt.xlabel("Diode Voltage, V (V)")
plt.ylabel("Diode Current, I (mA)")
plt.legend(title="Ambient Temperature")
plt.grid(True, linestyle="--", alpha=0.6)

plt.tight_layout()

# Save at the required resolution
plt.savefig("diode_iv.png", dpi=350)

plt.show()