# file kondensator-018
import numpy as np
import matplotlib.pyplot as plt

# Periode og spenning

#### KAN ENDRE Variabel ###########
f = 1  # [Hz]
U0 = 22  # [V]
tid = 1  # [s]
###################################

t = np.linspace(0, tid, 1000)  # [s]
U = U0 * np.sin(2 * np.pi * f * t)

plt.plot(t, U)
plt.xlabel("Tid [s]")
plt.ylabel("Spenning [V]")
plt.title(f"Frekvens: {f}Hz, $U_0 = {U0}$V")
plt.show()
