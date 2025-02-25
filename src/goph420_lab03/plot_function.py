import numpy as np 
import matplotlib.pyplot as plt

#S_max = np.sqrt(H ** 2 * (B1 ** -2 - B2 ** -2))
#S = (0.25 * f) * (2k + 1)
    
def Fz(Z, f):
   # densities in kg/m^3
   p1 = 1800
   p2 = 2500

   # velocities in m/s
   B1 = 1900
   B2 = 3200

   # thicknesses in m
   H = 4000
   return np.tan(2 * np.pi() * f * Z) - (p2 / p1) * np.sqrt((H**2) * (B1 **2 - B2 **2) -Z **2) / Z


def asymptote_finder(): 
    # densities in kg/m^3
    p1 = 1800
    p2 = 2500

    # velocities in m/s
    B1 = 1900
    B2 = 3200

    # thicknesses in m
    H = 4000 
        
    S_max = np.sqrt(H ** 2 * (B1 ** -2 - B2 ** -2))

    S_list = []
    k = np.linspace(0,S_max)
    f = 0.1
    while k <= S_max:
        S = (0.25 * f) * (2*k + 1)
        S_list.append(S)
    return S_list


