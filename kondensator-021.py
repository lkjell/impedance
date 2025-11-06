# file kondensator-021
# Ren spole AC
import numpy as np
import matplotlib.pyplot as plt

# CIVIL

f = 1  # frekvens [Hz]
U0 = 1  # [V] maks spenning
L = 2 * np.pi * f  # Henry

t = np.linspace(0, 3, 1000)  # s
U = U0 * np.sin(2 * np.pi * f * t)

# Integrerer med respekt til tiden
# U_L =  Ldi/dt => di = (U_L / L) dt
I = -np.cos(2 * np.pi * t) * (U0 / (2 * np.pi * f * L))
I2 = np.sin(2 * np.pi * t - np.pi / 2) * (U0 / (2 * np.pi * f * L))

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
axs[1].plot(t, I, color="r")
axs[1].set_xlabel("Tid [s]")
axs[1].set_ylabel("Strøm [A]")
axs[1].set_title("$I$")

fig.suptitle(f"AC spenning og strøm. Spole.")
plt.tight_layout()
plt.show()
