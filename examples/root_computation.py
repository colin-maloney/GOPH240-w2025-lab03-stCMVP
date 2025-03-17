from goph420_lab03.root_finding import root_newton_raphson
import numpy as np

def main():
    # Densities in kg/m^3
    p1 = 1800
    p2 = 2500

    # Velocities in m/s
    B1 = 1900
    B2 = 3200

    # Thickness in m
    H = 4000

    freq = [0.1, 0.5, 1.0, 1.5, 2.0]

    f = freq[0]

    def F(Z):
        C = (H ** 2) * (B1 ** -2 - B2 ** -2)
        return (((p2 / p1) * np.sqrt(C - Z ** 2) / Z)
                - np.tan(2 * np.pi * f * Z))
    def dfdz(Z):
        C = (H ** 2) * (B1 ** -2 - B2 ** -2)
        return ((-(p2/p1) * C/(Z**2 * np.sqrt(C - Z ** 2)))
                - 2*np.pi*f*(1/np.cos(2*np.pi*f*Z))**2)

    #Frequency = 0.1
    x0 = 1.1
    root1, iter, error = root_newton_raphson(x0, F, dfdz)
    print("For frequency 0.1")
    print("="*40)
    print(f"Root: {root1:.6}")
    print(f"Iteration: {iter}")
    print(f"Rel. Error: {error}")
    print("="*40)

if __name__ == '__main__':
    main()