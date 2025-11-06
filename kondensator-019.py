# file kondensator-019
import numpy as np
import matplotlib.pyplot as plt


# Spenning og Strøm resistans, AC

U0 = 10  # [V]
R = 1000  # [\ohm]
f = 1  # frekvens [Hz]
t = np.linspace(0, 2, 1000)  # s
U = U0 * np.sin(2 * np.pi * f * t)

I = U / R

fig, axs = plt.subplots(3, 1)

P = U * I

axs[0].plot(t, U)
axs[0].set_xlabel("Tid [s]")
axs[0].set_ylabel("Spenning [V]")
axs[0].set_title("$U$")


axs[1].plot(t, I, color="r")
axs[1].set_xlabel("Tid [s]")
axs[1].set_ylabel("Strøm [A]", color="r")
axs[1].set_title("$I$")

axs[2].plot(t, P, color="g")
axs[2].set_xlabel("Tid [s]")
axs[2].set_ylabel("Effekt [W]", color="g")
axs[2].set_title("$P$")

fig.suptitle(f"AC spenning og strøm")
plt.tight_layout()
plt.show()
