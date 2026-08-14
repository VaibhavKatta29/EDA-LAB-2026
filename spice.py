import numpy as np
import matplotlib.pyplot as plt

tox = 10e-7
W = 4e-4
L = 0.18e-4
mu_n = 400
eps_ox = 0.33 * 1e-12
Cox = eps_ox / tox
beta = mu_n * Cox * (W / L)
Vt = -0.48 #calculated manually 
l = 0.1
alpha = 1.1

vds = np.linspace(0, 4, 100)
vgs_list = [1, 2, 3]

plt.figure(1)
for vgs in vgs_list:
    id_l1 = np.where(vds < (vgs - Vt),
                     beta * (((vgs - Vt) * vds - 0.5 * vds**2)*(1+l*vds)),
                     0.5 * beta * (vgs - Vt)**2*(1+l*(vds)))
    id_l1 = np.maximum(id_l1, 0)
    plt.plot(vds, id_l1, label=f'VGS={vgs}V (SPICE Level 1)')

plt.xlabel('Vds (V)')
plt.ylabel('Id (A)')
plt.legend()
plt.grid(True)
plt.savefig('E12_MOSFET_lvl_1_Model', dpi=350)

plt.figure(2)

for vgs in vgs_list:
    id_l1 = np.where(vds < (vgs - Vt)/alpha,
                     beta * ((vgs - Vt) * vds - alpha*0.5 * vds**2)*(1+l*vds),
                     0.5 * (beta/alpha) * (vgs - Vt)**2*(1+l*(vds)))
    id_l1 = np.maximum(id_l1, 0)
    plt.plot(vds, id_l1, label=f'VGS={vgs}V (SPICE Level 3)')

plt.xlabel('Vds (V)')
plt.ylabel('Id (A)')
plt.legend()
plt.grid(True)
plt.savefig('E12_MOSFET_lvl_3_Model', dpi=350)
plt.show()