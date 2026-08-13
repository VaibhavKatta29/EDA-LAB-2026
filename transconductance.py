import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dft = pd.read_csv("MOSFET_ID_VGS.csv")

fig, ax = plt.subplots(1, 2, figsize=(11, 4.2))

peak_gm = -np.inf

for v_ds, g in dft.groupby("V_DS (V)"):

    g = g.sort_values("V_GS (V)")

    gm = np.gradient(g["I_D (mA)"], g["V_GS (V)"])

    ax[0].plot(
        g["V_GS (V)"],
        g["I_D (mA)"],
        linewidth=2,
        label=f"$V_{{DS}}$ = {v_ds} V"
    )

    ax[1].plot(
        g["V_GS (V)"],
        gm,
        linewidth=2,
        label=f"$V_{{DS}}$ = {v_ds} V"
    )

    # Find peak gm
    i = np.argmax(gm)

    # Find peak gm
i = np.argmax(gm)

if gm[i] > peak_gm:
    peak_gm = gm[i]
    peak_vgs = g["V_GS (V)"].iloc[i]
    peak_vds = v_ds

# Mark peak
ax[1].plot(peak_vgs, peak_gm, marker="o", markersize=8)

ax[1].annotate(
    f"Peak gm = {peak_gm:.2f} mS\nVGS = {peak_vgs:.2f} V",
    xy=(peak_vgs, peak_gm),
    xytext=(10, 10),
    textcoords="offset points"
)

ax[0].set_title("Transfer characteristics")
ax[0].set_xlabel("$V_{GS}$ (V)")
ax[0].set_ylabel("$I_D$ (mA)")

ax[1].set_title("Transconductance $g_m = dI_D/dV_{GS}$")
ax[1].set_xlabel("$V_{GS}$ (V)")
ax[1].set_ylabel("$g_m$ (mS)")

for a in ax:
    a.grid(True, linestyle="--", alpha=0.6)
    a.legend(fontsize=9)

plt.tight_layout()
plt.savefig("gm_transfer.png", dpi=300)
plt.show()

print("Peak gm =", peak_gm, "mS")
print("VGS at peak gm =", peak_vgs, "V")