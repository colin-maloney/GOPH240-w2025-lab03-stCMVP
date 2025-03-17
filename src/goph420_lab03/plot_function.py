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

    # Compute S_max
    S_max = np.sqrt(H ** 2 * (B1 ** -2 - B2 ** -2))

    # select some frequency values
    freq = [0.1, 0.5, 1.0, 1.5, 2.0]
    nf = len(freq)

    # Create subplots
    fig, axs = plt.subplots(nf, 1, figsize=(8, 10), sharex=True, sharey=True)
    fig.suptitle('Function plot using frequencies\n[0.1, 0.5, 1.0, 1.5, 2.0]', fontsize=14, fontweight='bold', y=0.95)

    for j, f in enumerate(freq):
        # define the function Fz
        def Fz(Z):
            return ((p2 / p1) * np.sqrt((H ** 2) * (B1 ** -2 - B2 ** -2) - Z ** 2) / Z) - np.tan(2 * np.pi * f * Z)

        # find asympototes
        atotes = [0.0]
        a = 0.0
        k = 0
        while k < S_max:
            a = (0.25 * 1 / f) * (2 * k + 1)
            if a < S_max:
                atotes.append(a)
            k += 1
        atotes.append(S_max)
        n = len(atotes)

        # plot the function
        ax = axs[j]  # Get the specific subplot axis
        for k, ak in enumerate(atotes):
            # plot the function
            if k < n - 1:
                zp = np.linspace(ak + 1e-3, atotes[k + 1] - 1e-3, 1000)
                Fp = Fz(zp)
                ax.plot(zp, Fp, '-r')
            if k <= n - 1:
                ax.plot([ak, ak], [-5, 5], '--b')
        ax.grid()
        ax.set_xlim(0, S_max)
        ax.set_ylim(-5, 5)
    fig.text(0.5, 0.04, 'Zeta', ha='center', fontsize=12)
    fig.text(0.04, 0.5, 'F(zeta)', va='center', rotation='vertical', fontsize=12)
    plt.subplots_adjust(hspace=0.5)
    plt.show()


if __name__ == "__main__":
    main()
