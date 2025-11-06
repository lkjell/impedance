# file kondensator-021
# Ren spole AC
import numpy as np
import matplotlib.pyplot as plt

# CIVIL

#### KAN ENDRE Variabel ###########
f = 1  # frekvens [Hz]
U0 = 1  # [V] maks spenning
L = 1 / (2 * np.pi * f)  # Induktans, henry [H]
tid = 3  # [s]
###################################

t = np.linspace(0, tid, 1000)  # s
U = U0 * np.sin(2 * np.pi * f * t)

# Integrerer med respekt til tiden
# U_L =  Ldi/dt => di = (U_L / L) dt
I = -np.cos(2 * np.pi * f * t) * (U0 / (2 * np.pi * f * L))
I = np.sin(2 * np.pi * f * t - np.pi / 2) * (U0 / (2 * np.pi * f * L))
I0 = U0 / (2 * np.pi * f * L)  # [A] maks strøm

P = U * I

fig, axs = plt.subplots(2, 1)

axs[0].plot(t, U)
ax = axs[0].twinx()
ax.plot(t, I, color="r")
# ax.tick_params(axis="y")
ax.set_ylabel("Strøm [A]", color="r")

axs[0].set_xlabel("Tid [s]")
axs[0].set_ylabel("Spenning [V]")
axs[0].set_title("$U$ og $I$")
axs[0].grid(True)

axs[1].plot(t, P, color="g")
axs[1].set_xlabel("Tid [s]")
axs[1].set_ylabel("Effekt [W]", color="g")
axs[1].set_title("$P$")
axs[1].grid(True)

fig.suptitle(
    f"AC Spole: $f = {f}$Hz, $U_0 = {U0}$V, "
    f"$I_0 = {I0:.3}$A, $L = {L:.3}$F, $\\theta = -90\\degree$"
)
plt.tight_layout()
plt.show()
