# file kondensator-020
# Ren kondensator AC
import numpy as np
import matplotlib.pyplot as plt

# CIVIL

f = 1  # frekvens [Hz]
U0 = 1  # [V] maks spenning
C = 1 / (2 * np.pi * f)

t = np.linspace(0, 3, 1000)  # s
U = U0 * np.sin(2 * np.pi * f * t)

# Derivere med respekt til tiden
# Q = C*U => dQ/dt = i (strøm)
I = C * U0 * np.cos(2 * np.pi * f * t) * 2 * np.pi * f
I = C * U0 * np.sin(2 * np.pi * f * t + np.pi / 2) * 2 * np.pi * f

fig, axs = plt.subplots(2, 1)

axs[0].plot(t, U)
ax = axs[0].twinx()
ax.plot(t, I, color="r")
# ax.tick_params(axis="y")
ax.set_ylabel("Strøm [A]", color="r")

axs[0].set_xlabel("Tid [s]")
axs[0].set_ylabel("Spenning [V]")
axs[0].set_title("$U$")


axs[1].plot(t, I, color="r")
axs[1].set_xlabel("Tid [s]")
axs[1].set_ylabel("Strøm [A]")
axs[1].set_title("$I$")

fig.suptitle(f"AC spenning og strøm. Kondensator.")
plt.tight_layout()
plt.show()
