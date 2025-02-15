import numpy as np
import matplotlib.pyplot as plt

# Figure 1: Hubble Tension Comparison
def plot_hubble_tension():
    # Data points from Riess et al. (2021) and Planck Collaboration (2020)
    local_h0 = 73.04  # Local Hubble constant measurement (km/s/Mpc)
    local_h0_err = 1.04  # Uncertainty
    cmb_h0 = 67.4  # CMB-derived Hubble constant (km/s/Mpc)
    cmb_h0_err = 0.5  # Uncertainty
    
    # Predicted Hubble constant with entropy-driven corrections
    predicted_h0 = 70.2  # Example value from the model
    predicted_h0_err = 0.8  # Example uncertainty

    # Plot
    fig, ax = plt.subplots(1, 2, figsize=(12, 6), sharey=True)

    # Left subplot: Local vs. CMB measurements
    ax[0].errorbar([1], [local_h0], yerr=[local_h0_err], fmt='o', color='blue', label='Local Measurements')
    ax[0].errorbar([2], [cmb_h0], yerr=[cmb_h0_err], fmt='o', color='green', label='CMB-Derived')
    ax[0].set_xticks([1, 2])
    ax[0].set_xticklabels(['Local', 'CMB'])
    ax[0].set_ylabel('Hubble Constant $H_0$ (km/s/Mpc)')
    ax[0].set_title('Observed Hubble Tension')
    ax[0].legend()

    # Right subplot: Predicted vs. Observed
    ax[1].errorbar([1], [predicted_h0], yerr=[predicted_h0_err], fmt='o', color='red', label='Entropy-Driven Prediction')
    ax[1].errorbar([2], [local_h0], yerr=[local_h0_err], fmt='o', color='blue', label='Local Measurements')
    ax[1].errorbar([3], [cmb_h0], yerr=[cmb_h0_err], fmt='o', color='green', label='CMB-Derived')
    ax[1].set_xticks([1, 2, 3])
    ax[1].set_xticklabels(['Prediction', 'Local', 'CMB'])
    ax[1].set_title('Entropy-Driven Resolution')
    ax[1].legend()

    plt.tight_layout()
    plt.savefig('hubble_tension.png')
    plt.show()

# Figure 2: Dark Matter Distribution
def plot_dark_matter_distribution():
    # Simulated dark matter distribution (example data)
    x = np.linspace(0, 10, 100)
    simulated_dm = np.exp(-x**2 / 10) + 0.1 * np.random.normal(size=len(x))
    observed_dm = np.exp(-x**2 / 10) + 0.05 * np.random.normal(size=len(x))

    # Entropy gradient (color scale)
    entropy_gradient = np.sin(x) + 1  # Arbitrary entropy function

    # Plot
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))

    # Left subplot: Simulated dark matter distribution
    sc1 = ax[0].scatter(x, simulated_dm, c=entropy_gradient, cmap='viridis', label='Simulated DM')
    ax[0].set_xlabel('Distance (Mpc)')
    ax[0].set_ylabel('Dark Matter Density')
    ax[0].set_title('Simulated Dark Matter Distribution')
    fig.colorbar(sc1, ax=ax[0], label='Entropy Gradient')

    # Right subplot: Observed weak lensing map
    sc2 = ax[1].scatter(x, observed_dm, c=entropy_gradient, cmap='viridis', label='Observed DM')
    ax[1].set_xlabel('Distance (Mpc)')
    ax[1].set_title('Observed Weak Lensing Map')
    fig.colorbar(sc2, ax=ax[1], label='Entropy Gradient')

    plt.tight_layout()
    plt.savefig('dark_matter_distribution.png')
    plt.show()

# Figure 3: CMB Spectral Distortion
def plot_cmb_spectral_distortion():
    # Frequency range
    freq = np.linspace(1, 1000, 1000)  # GHz
    current_limit = 1e-7 * np.ones_like(freq)  # Current upper limit
    predicted_distortion = 5e-9 * np.exp(-((freq - 200) / 50)**2)  # Predicted distortion

    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(freq, current_limit, label='Current Upper Limit', linestyle='--', color='blue')
    ax.plot(freq, predicted_distortion, label='Predicted Distortion', color='red')
    ax.set_xlabel('Frequency (GHz)')
    ax.set_ylabel('Spectral Distortion Amplitude')
    ax.set_title('CMB Spectral Distortion')
    ax.legend()
    ax.set_yscale('log')
    plt.tight_layout()
    plt.savefig('cmb_spectral_distortion.png')
    plt.show()

# Figure 4: Quantum Decoherence Rate
def plot_quantum_decoherence():
    # Decoherence rate as a function of system size
    system_size = np.linspace(1, 100, 100)  # Arbitrary units
    standard_rate = 1e-3 * np.exp(-system_size / 50)  # Standard decoherence rate
    entropic_rate = 1e-3 * np.exp(-system_size / 50) + 1e-5 * system_size  # Entropy-modified rate

    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(system_size, standard_rate, label='Standard Decoherence', color='blue')
    ax.plot(system_size, entropic_rate, label='Entropy-Modified Decoherence', color='red')
    ax.set_xlabel('System Size (Arbitrary Units)')
    ax.set_ylabel('Decoherence Rate')
    ax.set_title('Quantum Decoherence Rate')
    ax.legend()
    plt.tight_layout()
    plt.savefig('quantum_decoherence.png')
    plt.show()

# Figure 5: Primordial Power Spectrum
def plot_primordial_power_spectrum():
    # Wavenumber range
    k = np.logspace(-4, 2, 100)  # Mpc^-1
    standard_spectrum = k**(-3)  # Standard power spectrum
    entropy_modified = k**(-3) * (1 + 0.1 * np.sin(np.log(k)))  # Entropy-modified spectrum

    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.loglog(k, standard_spectrum, label='Standard Spectrum', color='blue')
    ax.loglog(k, entropy_modified, label='Entropy-Modified Spectrum', color='red')
    ax.set_xlabel('Wavenumber $k$ (Mpc$^{-1}$)')
    ax.set_ylabel('Power Spectrum $P(k)$')
    ax.set_title('Primordial Power Spectrum')
    ax.legend()
    plt.tight_layout()
    plt.savefig('primordial_power_spectrum.png')
    plt.show()

# Generate all figures
if __name__ == "__main__":
    plot_hubble_tension()
    plot_dark_matter_distribution()
    plot_cmb_spectral_distortion()
    plot_quantum_decoherence()
    plot_primordial_power_spectrum()
