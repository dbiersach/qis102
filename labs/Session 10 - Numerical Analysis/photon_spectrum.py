# photon_spectrum.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d


def main():
    file_name = "photon_spectrum.txt"
    file_path = Path(__file__).parent / file_name
    # Note: this is NOT a CSV file and has no header row
    samples = np.genfromtxt(file_path, delimiter=" ")
    energy, density = samples.T

    min_energy, max_energy = np.min(energy), np.max(energy)
    energy_est = np.linspace(min_energy, max_energy, 1000)

    density_f = interp1d(energy, density, kind="cubic")
    density_est = density_f(energy_est)

    min_window, max_window = 2.12, 3.45  # MeV
    window_energy = quad(density_f, min_window, max_window)[0]
    total_energy = quad(density_f, min_energy, max_energy)[0]
    print(f"{window_energy/total_energy:.4%}", end=" ")
    print("of the beam photons are within the energy window")

    plt.figure(Path(__file__).name)
    plt.scatter(energy, density, zorder=3)

    plt.plot(energy_est, density_est)
    plt.fill_between(
        energy_est,
        density_est,
        where=(energy_est >= min_window) * (energy_est <= max_window),
        color="orange",
    )

    plt.xlabel("Photon Energy [MeV]")
    plt.ylabel(r"Density of photons ($\;J/m^3\;x\;10^7$)")
    plt.title("Photon Spectrum")
    plt.axhline(0, c="k")
    plt.show()


main()
