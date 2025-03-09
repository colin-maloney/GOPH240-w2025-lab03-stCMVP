import numpy as np
import matplotlib.pyplot as plt

#S_max = np.sqrt(H ** 2 * (B1 ** -2 - B2 ** -2))
#S = (0.25 * f) * (2k + 1)
def main(): 
    # Densities in kg/m^3
    p1 = 1800
    p2 = 2500

    # Velocities in m/s
    B1 = 1900
    B2 = 3200

    # Thickness in m
    H = 4000

    # Compute S_max
    S_max = np.sqrt(H ** 2 * (B1 ** -2 - B2 ** -2))

    # select some frequency values 
    freq = [0.1, 0.5, 1.0, 1.5, 2.0] 
    nf = len(freq) 

    for j, f in enumerate(freq): 
        # define the function Fz 
        def Fz(Z): 
            return (p2 / p1) * np.sqrt((H ** 2) * (B1 ** -2 - B2 ** -2) - Z ** 2) / Z - np.tan(2 * np.pi * f * Z)
    
    # find asympototes 
    atotes = [0.0] 
    a = 0.0 
    k = 0
    while k <= S_max:
        a = (0.25 * 1/f) * (2 * k + 1)
        if a < S_max:
            atotes.append(a)
        k += 1
    atotes.append(S_max) 
    n = len(atotes)

    # plot the function 
    plt.subplot(nf, 1, j+1)
    for k, ak in enumerate(atotes): 
        # plot the asymptotes 
        if k and k < n - 1:
            plt.plot([ak, ak], [-5, 5], '--b') 
        # plot the function 
        if k < n-1:
            zp = np.linspace(ak + 1e-3, atotes[k+1] - 1e-3)
            Fp = Fz(zp)
            plt.plot(zp, Fp, '-r') 
    plt.grid() 
    plt.xlabel('Zeta') 
    plt.ylabel('F(zeta)') 
    plt.xlim(0, S_max)
    plt.ylim(-5, 5) 
plt.show()

if __name__ == "__main__": 
    main()



