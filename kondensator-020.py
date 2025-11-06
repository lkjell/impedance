# file kondensator-020
# Ren kondensator AC
import numpy as np
import matplotlib.pyplot as plt

# CIVIL

#### KAN ENDRE Variabel ###########
f = 1  # frekvens [Hz]
U0 = 1  # [V] maks spenning
C = 1 / (2 * np.pi * f)  # Kapasitans, farad [F]
tid = 3  # [s]
###################################

t = np.linspace(0, tid, 1000)  # s
U = U0 * np.sin(2 * np.pi * f * t)

# Derivere med respekt til tiden
# Q = C*U => dQ/dt = i (strøm)
I = C * U0 * np.cos(2 * np.pi * f * t) * 2 * np.pi * f
I = C * U0 * np.sin(2 * np.pi * f * t + np.pi / 2) * 2 * np.pi * f
I0 = C * U0 * 2 * np.pi * f  # [A] maks strøm

P = U * I

fig, axs = plt.subplots(2, 1)

axs[0].plot(t, U)
ax = axs[0].twinx()
ax.plot(t, I, color="r")
ax.set_ylabel("Strøm [A]", color="r")

axs[0].set_xlabel("Tid [s]")
axs[0].set_ylabel("Spenning [V]")
axs[0].set_title("$U$")
axs[0].grid(True)

axs[1].plot(t, P, color="g")
axs[1].set_xlabel("Tid [s]")
axs[1].set_ylabel("Effekt [W]", color="g")
axs[1].set_title("$P$")
axs[1].grid(True)

fig.suptitle(
    f"AC kondensator: $f = {f}$Hz, $U_0 = {U0}$V, "
    f"$I_0 = {I0:.3}$A, $C = {C:.3}$F, $\\theta = 90\\degree$"
)
plt.tight_layout()
plt.show()
