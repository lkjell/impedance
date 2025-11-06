# file kondensator-018
import numpy as np
import matplotlib.pyplot as plt

# Periode og spenning

f = 1
t = np.linspace(0, 1, 1000)  # s
U0 = 22
U = U0 * np.sin(2 * np.pi * f * t)

plt.plot(t, U)
plt.xlabel("Tid [s]")
plt.ylabel("Spenning [V]")
plt.show()
