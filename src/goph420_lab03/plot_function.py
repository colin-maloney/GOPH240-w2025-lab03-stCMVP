import numpy as np
import matplotlib.pyplot as plt

    
def Fz(Z, f):
   # densities in kg/m^3
   p1 = 1800
   p2 = 2500

   # velocities in m/s
   B1 = 1900
   B2 = 3200

   # thicknesses in m
   H = 4000
   return np.tan(2 * np.pi * f * Z) - (p2 / p1) * np.sqrt((H**2) * (B1 ** 2 - B2 ** 2) - Z ** 2) / Z




def asymptote_finder():
    # Velocities in m/s
    B1 = 1900
    B2 = 3200

    # Thickness in m
    H = 4000

    # Compute S_max
    Z_max = np.sqrt(H ** 2 * (B1 ** -2 - B2 ** -2))

    Z_list = []
    Z_list.append(0)
    k = 0
    f = 1
    Z = 0

    while Z <= Z_max:
        Z = (0.25 * 1/f) * (2 * k + 1)
        if Z < Z_max:
            Z_list.append(Z)
        k += 1
    Z_list.append(Z_max)

    return Z_list

def main():
    # Velocities in m/s
    B1 = 1900
    B2 = 3200

    # Thickness in m
    H = 4000

    Z_max = np.sqrt(H ** 2 * (B1 ** -2 - B2 ** -2))
    Z_list = asymptote_finder()
    freqs = [0.1, 0.5, 1, 2]
    nfreqs = len(freqs)
    

    for i in range(len(x_values)):
         plt.plot(S_list[i],)
             if np.isclose(function_values[i], asymptote):
                 function_values[i] = np.nan







