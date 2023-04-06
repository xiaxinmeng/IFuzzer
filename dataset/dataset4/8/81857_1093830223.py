
import cmath
import numpy as np

z=255*np.ones((3,3)) * np.exp(1j * np.pi*np.ones((3,3)))

def get_k_amp_array(z):
    return abs(z)

def get_k_ph_array(z):
    return np.array([[cmath.phase(z_row) for z_row in z_col] for z_col in z ])

amp_array=  get_k_amp_array(z)
ph_array=   get_k_ph_array(z)

print(amp_array)
print(ph_array)
