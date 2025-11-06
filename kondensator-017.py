# file kondensator-017
import numpy as np
import matplotlib.pyplot as plt

# Resistor
# Debouncing switches1 kΩ – 100 kΩ
# Timing circuits (e.g. 555)10 kΩ – 1 MΩ
# Audio filters1 kΩ – 100 kΩ
# Power supply smoothing10 Ω – 1 kΩ

# Capacitor
# Ceramic1 pF – 1 µF Decoupling, filtering
# Electrolytic1 µF – 10,000 µF Power supply smoothing
# Tantalum0.1 µF – 470 µF
# Stable filtering, compact size
# Film1 nF – 10 µF Audio, precision circuits
# Supercapacitors 0.1 F – 5000 F Energy storage, backup power

# Spenning over kondensator Utladning

#### KAN ENDRE Variabel ###########
U = 10  # [V]
R = 10**6  # 1 [Mohm]
C = 10**-6  # 1 [uF]
tid = 10  # [s]
###################################

t = np.linspace(0, tid, 1000)  # s
Uc = U * np.exp(-t / (R * C))


fig, axs = plt.subplots(3, 1)

axs[0].plot(t, Uc)
axs[0].set_xlabel("Tid [s]")
axs[0].set_ylabel("Spenning [V]")
axs[0].set_title("Spenning over kondensator $U_C$")

Ic = (U / R) * np.exp(-t / (R * C))
Ur = Ic * R

axs[1].plot(t, Ur)
axs[1].set_xlabel("Tid [s]")
axs[1].set_ylabel("Spenning [V]")
axs[1].set_title("Spenning over motstand $U_R$")


axs[2].plot(t, Ic)
axs[2].set_xlabel("Tid [s]")
axs[2].set_ylabel("Strøm [A]")
axs[2].set_title("Strømmen gjennom kondensator $I_C$")

fig.suptitle(f"R: {R:.0e}, C: {C:.0e}, $\\tau$:{R*C:.0e}")
plt.tight_layout()
plt.show()
