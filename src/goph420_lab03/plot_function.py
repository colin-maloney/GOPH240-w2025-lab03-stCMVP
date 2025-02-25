import numpy as np 
import matplotlib.pyplot as plt 

def main_function(x):
    
    # densities in kg/m^3
    p1 = 1800 
    p2 = 2500 
    
    #velocities in m/s
    B1 = 1900 
    B2 = 3200 
   
    # thicknesses in m
    H = 4000
    
   def Fz(p1, p2, B1, B2, f, Z): = np.tan(2*np.pi()*f*Z) - (p2 / p1) * np.sqrt((H**2) * (B1 **2 - B2 **2) -Z **2) / Z 
    
    return Fz
    
  
pass