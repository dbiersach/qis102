# fourier_filter.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator


def f(x):
    return 29 * np.cos(3 * x) + 7 * np.sin(40 * x)


def dft(ts, ys):
    num_samples = ts.size
    num_terms = int(num_samples / 2)  # Nyquist limit
    ct = np.zeros(num_terms, dtype=complex)
    for term in range(0, num_terms):
        for sample in range(0, num_samples):
            ct[term] += ys[sample] * np.exp(complex(0, -(term * ts[sample])))
    ct = ct * 2 / num_samples
    ct[0] /= 2  # DC value should NOT be doubled
    return ct


def idft(ts, ct):
    num_samples = ts.size
    num_terms = ct.size
    yr = np.zeros(num_samples, dtype=complex)
    for sample in range(0, num_samples):
        for term in range(0, num_terms):
            yr[sample] += ct[term] * np.exp(complex(0, (term * ts[sample])))
    return yr


def plot_samples(ax, ts, ys):
    num_samples = ts.size
    ax.plot(ts, ys, color="lightgray", linewidth=1)
    ax.scatter(ts, ys, color="black", marker=".", s=10.0, zorder=2)
    ax.set_title(f"Sampled Wave ({num_samples} samples)")
    ax.set_xlabel("scaled time", loc="right")
    ax.set_ylabel("amplitude")


def plot_dft(ax, ct):
    num_terms = 50
    # fmt: off
    ax.bar(range(0, num_terms), np.abs(ct.real[:num_terms]),
        color="blue", label="cosine", zorder=2)
    ax.bar(range(0, num_terms), np.abs(ct.imag[:num_terms]),
        color="red",  label="sine", zorder=2)
    # fmt: on
    ax.grid(which="major", axis="x", color="black", linewidth=1)
    ax.grid(which="minor", axis="x", color="lightgray", linewidth=1)
    ax.grid(which="major", axis="y", color="black", linewidth=1)
    ax.grid(which="minor", axis="y", color="lightgray", linewidth=1)

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.set_title("Discrete Fourier Transform")
    ax.set_xlabel("frequency", loc="right")
    ax.set_ylabel("amplitude")
    ax.legend(loc="upper right")


def plot_idft(ax, ts, yr):
    num_samples = ts.size
    ax.plot(ts, yr, color="purple")
    ax.set_title(f"Inverse DFT ({num_samples} samples)")
    ax.set_xlabel("scaled time", loc="right")
    ax.set_ylabel("amplitude")


def plot_power_spectrum(ax, ct):
    num_terms = 50
    ax.bar(
        range(0, num_terms), abs(ct[:num_terms]), color="green", label="sine", zorder=2
    )
    ax.grid(which="major", axis="x", color="black", linewidth=1)
    ax.grid(which="minor", axis="x", color="lightgray", linewidth=1)
    ax.grid(which="major", axis="y", color="black", linewidth=1)
    ax.grid(which="minor", axis="y", color="lightgray", linewidth=1)

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.set_title("Power Spectrum")
    ax.set_xlabel("frequency", loc="right")
    ax.set_ylabel(r"$\Vert amplitude \Vert$")


def main():
    plt.figure(Path(__file__).name, figsize=(12, 8), constrained_layout=True)

    sample_duration = 2 * np.pi
    num_samples = 1000

    ts = np.linspace(0, sample_duration, num_samples, endpoint=False)
    ys = f(ts)

    ct = dft(ts, ys)

    plot_samples(plt.subplot(2, 2, 1), ts, ys)
    plot_dft(plt.subplot(2, 2, 2), ct)

    # Filter out high-frequency noise
    # ct[40] = 0

    yr = idft(ts, ct)

    plot_idft(plt.subplot(2, 2, 3), ts, np.real(yr))
    plot_power_spectrum(plt.subplot(2, 2, 4), ct)

    plt.show()


main()
