import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = "MOSFET_ID_VDS.csv"
df = pd.read_csv(file_path)

# Plot one curve for each gate voltage
for vgs, group in df.groupby("V_GS (V)"):
    plt.plot(
        group["V_DS (V)"],
        group["I_D (mA)"],
        marker="o",
        label=f"V_GS = {vgs} V"
    )

# Labels and title
plt.xlabel("V_DS (V)")
plt.ylabel("I_D (mA)")
plt.title("MOSFET I_D-V_DS Characteristics")

# Grid and legend
plt.grid(True)
plt.legend()

# Save figure at 300 dpi
plt.savefig("ID_VDS_Family.png", dpi=300)

# Display the graph
plt.show()