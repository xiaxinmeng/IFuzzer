import numpy as np
n=2.758
n2 = 2.0 / n
ct = np.cos(2 * np.pi * 2.0 / 5)
print("numpy", ct, abs(ct ** n2) * 5.0)