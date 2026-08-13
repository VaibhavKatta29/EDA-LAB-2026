import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 1. Load the CSV file
file_path = "MOSFET_ID_VDS.csv"

try:
    df = pd.read_csv(file_path)
    print("CSV file successfully loaded!")
    print(df.columns)
except FileNotFoundError:
    print(f"Error: Could not find '{file_path}'. Check the path and try again.")
    exit()

# 2. Plot ID vs VDS
plt.figure(1, figsize=(10, 6))

for v_gs, group in df.groupby("V_GS (V)"):
    plt.plot(
        group["V_DS (V)"],
        group["I_D (mA)"],
        marker="o",
        linewidth=2,
        label=f"$V_{{GS}}$ = {v_gs} V"
    )

plt.title("MOSFET Output Characteristics ($I_D$ vs $V_{DS}$)",
          fontsize=14, fontweight="bold", pad=15)
plt.xlabel("Drain-to-Source Voltage, $V_{DS}$ (V)",
           fontsize=12, labelpad=10)
plt.ylabel("Drain Current, $I_D$ (mA)",
           fontsize=12, labelpad=10)
plt.legend(title="Gate-Source Voltage")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

plt.savefig("id_vds.png", dpi=300)


# 3. Calculate and plot differential output conductance
plt.figure(2, figsize=(10, 6))

for v_gs, group in df.groupby("V_GS (V)"):

    v_ds = group["V_DS (V)"]
    i_d = group["I_D (mA)"]

    # gd = dID / dVDS
    did_dvds = np.gradient(i_d, v_ds)

    plt.plot(
        v_ds,
        did_dvds,
        marker="s",
        linestyle="--",
        linewidth=2,
        label=f"$V_{{GS}}$ = {v_gs} V"
    )

plt.title("MOSFET Differential Output Conductance "
          "($g_d = dI_D/dV_{DS}$)",
          fontsize=14, fontweight="bold", pad=15)
plt.xlabel("Drain-to-Source Voltage, $V_{DS}$ (V)",
           fontsize=12, labelpad=10)
plt.ylabel("Conductance, $g_d$ (mS or mA/V)",
           fontsize=12, labelpad=10)
plt.legend(title="Gate-Source Voltage")
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()

plt.savefig("gd_vds.png", dpi=300)

# 4. Display the figures
plt.show()