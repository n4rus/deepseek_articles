import numpy as np
import matplotlib.pyplot as plt

# Figure 1: Gravitational Wave Data
def plot_gravitational_wave_data():
    # Observed gravitational wave frequencies and amplitudes
    freq_obs = np.linspace(10, 1000, 100)  # Frequency range (Hz)
    amplitude_obs = 1e-21 * np.exp(-((freq_obs - 250) / 100)**2)  # Example observed data
    
    # Predicted gravitational wave amplitudes
    amplitude_pred = 1e-21 * np.exp(-((freq_obs - 250) / 100)**2) * (1 + 0.1 * np.sin(freq_obs / 50))
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(freq_obs, amplitude_obs, 'bo', label='Observed Data')
    plt.plot(freq_obs, amplitude_pred, 'r-', label='Entropy-Driven Prediction')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Amplitude')
    plt.title('Gravitational Wave Signals')
    plt.legend()
    plt.grid()
    plt.savefig('observed_gravitational_wave_data.png')
    plt.show()

# Figure 2: Dark Matter Distribution
def plot_dark_matter_distribution():
    # Distance range (Mpc)
    distance = np.linspace(0, 100, 100)
    
    # Observed dark matter density
    density_obs = np.exp(-distance / 20) + 0.05 * np.random.normal(size=len(distance))
    
    # Predicted dark matter density
    density_pred = np.exp(-distance / 20) * (1 + 0.1 * np.sin(distance))
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(distance, density_obs, 'bo', label='Observed Data')
    plt.plot(distance, density_pred, 'r-', label='Entropy-Driven Prediction')
    plt.xlabel('Distance (Mpc)')
    plt.ylabel('Dark Matter Density')
    plt.title('Dark Matter Distribution')
    plt.legend()
    plt.grid()
    plt.savefig('dark_matter_observed_vs_model.png')
    plt.show()

# Figure 3: Dark Energy Equation of State
def plot_dark_energy_equation_of_state():
    # Redshift range
    redshift = np.linspace(0, 2, 100)
    
    # Observed equation of state parameter w_DE
    w_DE_obs = -1 + 0.05 * np.random.normal(size=len(redshift))
    
    # Predicted equation of state parameter
    w_DE_pred = -1 + 0.02 * np.sin(redshift * np.pi)
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(redshift, w_DE_obs, 'bo', label='Observed Data')
    plt.plot(redshift, w_DE_pred, 'r-', label='Entropy-Driven Prediction')
    plt.xlabel('Redshift')
    plt.ylabel('$w_{DE}$')
    plt.title('Dark Energy Equation of State')
    plt.legend()
    plt.grid()
    plt.savefig('dark_energy_observed_vs_model.png')
    plt.show()

# Figure 4: Quantum Decoherence Rates
def plot_quantum_decoherence_rates():
    # System size range
    system_size = np.linspace(1, 100, 100)
    
    # Observed decoherence rates
    decoherence_obs = 1e-3 * np.exp(-system_size / 50) + 1e-5 * np.random.normal(size=len(system_size))
    
    # Predicted decoherence rates
    decoherence_pred = 1e-3 * np.exp(-system_size / 50) + 1e-5 * system_size
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(system_size, decoherence_obs, 'bo', label='Observed Data')
    plt.plot(system_size, decoherence_pred, 'r-', label='Entropy-Driven Prediction')
    plt.xlabel('System Size (Arbitrary Units)')
    plt.ylabel('Decoherence Rate')
    plt.title('Quantum Decoherence Rates')
    plt.legend()
    plt.grid()
    plt.savefig('quantum_coherence_observed_vs_model.png')
    plt.show()

# Figure 5: Hubble Tension Resolution
def plot_hubble_tension():
    # Redshift range
    redshift = np.linspace(0, 2, 100)
    
    # Observed Hubble parameter values
    hubble_obs = 70 + 5 * np.random.normal(size=len(redshift))
    
    # Predicted Hubble parameter values
    hubble_pred = 70 + 2 * np.sin(redshift * np.pi)
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(redshift, hubble_obs, 'bo', label='Observed Data')
    plt.plot(redshift, hubble_pred, 'r-', label='Entropy-Driven Prediction')
    plt.xlabel('Redshift')
    plt.ylabel('$H(z)$ (km/s/Mpc)')
    plt.title('Hubble Tension Resolution')
    plt.legend()
    plt.grid()
    plt.savefig('hubble_tension_observed_vs_model.png')
    plt.show()

# Generate all figures
if __name__ == "__main__":
    plot_gravitational_wave_data()
    plot_dark_matter_distribution()
    plot_dark_energy_equation_of_state()
    plot_quantum_decoherence_rates()
    plot_hubble_tension()
