import numpy as np
import matplotlib.pyplot as plt

# Given parameters
Is = 1e-12
Vt = 0.02585
n_values = [1.0, 1.5, 2.0]

# Diode voltage sweep
Vd = np.arange(0, 0.81, 0.01)


# --------------------------------------------------
# 1. Normal I-V plot
# --------------------------------------------------

plt.figure(figsize=(10, 6))

for n in n_values:

    Id = Is * (np.exp(Vd / (n * Vt)) - 1)

    plt.plot(Vd, Id, linewidth=2, label=f'n = {n}')

plt.xlabel('$V_D$ (V)')
plt.ylabel('$I_D$ (A)')
plt.title('Diode I-V Characteristics')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('diode_iv.png', dpi=350)


# --------------------------------------------------
# 2. Logarithmic I-V plot
# --------------------------------------------------

plt.figure(figsize=(10, 6))

for n in n_values:

    Id = Is * (np.exp(Vd / (n * Vt)) - 1)

    plt.plot(Vd, Id, linewidth=2, label=f'n = {n}')

plt.yscale('log')
plt.xlabel('$V_D$ (V)')
plt.ylabel('$I_D$ (A)')
plt.title('Diode I-V Characteristics - Log Scale')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('diode_iv_log.png', dpi=350)


# --------------------------------------------------
# 3. Small-signal conductance
# --------------------------------------------------

plt.figure(figsize=(10, 6))

for n in n_values:

    Id = Is * (np.exp(Vd / (n * Vt)) - 1)

    gd = np.gradient(Id, Vd)

    plt.plot(Vd, gd, linewidth=2, label=f'n = {n}')

plt.yscale('log')
plt.xlabel('$V_D$ (V)')
plt.ylabel('$g_d$ (S)')
plt.title('Diode Small-Signal Conductance')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('diode_gd.png', dpi=350)


plt.show()