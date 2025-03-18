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

    def F(Z,f):
        C = (H ** 2) * (B1 ** -2 - B2 ** -2)
        return (((p2 / p1) * np.sqrt(C - Z ** 2) / Z)
                - np.tan(2 * np.pi * f * Z))
    def dfdz(Z,f):
        C = (H ** 2) * (B1 ** -2 - B2 ** -2)
        return ((-(p2/p1) * C/(Z**2 * np.sqrt(C - Z ** 2)))
                - 2*np.pi*f*(1/np.cos(2*np.pi*f*Z))**2)

    def asymptotes(f,H,B1,B2):
        atotes = [0.0]
        a = 0.0
        k = 0
        S_max = np.sqrt(H ** 2 * (B1 ** -2 - B2 ** -2))
        while a < S_max:
            a = (0.25 * 1 / f) * (2 * k + 1)
            if a < S_max:
                atotes.append(a)
            k += 1
        atotes.append(S_max)
        n = len(atotes)
        return atotes

    S_max = np.sqrt(H ** 2 * (B1 ** -2 - B2 ** -2))
    initial_guess = []
    for i in range(freq):
        asymptotes = asymptotes(i,H,B1,B2)
        F = F(Z, freq(i))
        dfdz = dfdz(Z,freq(i))
        for j in range(len(asymptotes)):
            if asymptotes[j] != 0 or S_max:
                x0 = asymptotes[j] - 1e-3
                initial_guess.append(x0)
                for j in range(len(initial_guess)):
                    roots = []
                    values = root_newton_raphson(initial_guess[j], F, dfdz)
                    roots.append(values)
                    print(roots)








if __name__ == '__main__':
    main()