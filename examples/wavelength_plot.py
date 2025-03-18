from goph420_lab03.root_finding import root_newton_raphson
import numpy as np
import matplotlib.pyplot as plt

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

    def get_asymptotes(f,H,B1,B2):
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
        return atotes

    S_max = np.sqrt(H ** 2 * (B1 ** -2 - B2 ** -2))
    root_modes = [[],[],[]]
    for f in freq:
        asymptotes = get_asymptotes(f,H,B1,B2)

        def F(Z):
            C = (H ** 2) * (B1 ** -2 - B2 ** -2)
            return (((p2 / p1) * np.sqrt(C - Z ** 2) / Z)
                    - np.tan(2 * np.pi * f * Z))

        def dfdz(Z):
            C = (H ** 2) * (B1 ** -2 - B2 ** -2)
            return ((-(p2 / p1) * C / (Z ** 2 * np.sqrt(C - Z ** 2)))
                    - 2 * np.pi * f * (1 / np.cos(2 * np.pi * f * Z)) ** 2)

        initial_guess = []
        for j, a in enumerate(asymptotes):
            if a == 0 or (a == S_max and F(a) > 0):
                continue
            x0 = asymptotes[j] - 1e-3
            initial_guess.append(x0)

        roots = []
        for x0 in initial_guess:
            values = root_newton_raphson(x0, F, dfdz)[0]
            roots.append(values)

        for k, mode in enumerate(root_modes):
            if k < len(roots):
                mode.append(roots[k])

    root_modes = np.array(root_modes, dtype=object)

    c_L0 = [np.sqrt(1 / (B1**-2 - (r/H)**2)) for r in root_modes[0]]
    c_L1 = [np.sqrt(1 / (B1**-2 - (r/H)**2)) for r in root_modes[1]]
    c_L2 = [np.sqrt(1 / (B1**-2 - (r/H)**2)) for r in root_modes[2]]

    wavelength0 = []
    for i, vel in enumerate(c_L0):
        wavelength0.append(vel/freq[i])

    wavelength1 = []
    for i, vel in enumerate(c_L1):
        wavelength1.append(vel/freq[i+1])

    wavelength2 = []
    for i, vel in enumerate(c_L2):
        wavelength2.append(vel/freq[i+2])

    plt.plot(freq[-len(wavelength0):], wavelength0, label='mode 0')
    plt.plot(freq[-len(wavelength1):], wavelength1, label='mode 1')
    plt.plot(freq[-len(wavelength2):], wavelength2, label='mode 2')

    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Wavelength (nm)')
    plt.title('Wavelength vs. Frequency for Modes 0, 1, 2', weight='bold')
    plt.grid()
    plt.legend()
    plt.savefig('../figures/mode_wavelength.png')


if __name__ == '__main__':
    main()