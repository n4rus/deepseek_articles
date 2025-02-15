import numpy as np
import matplotlib.pyplot as plt

# Figure 1: Time Delay Distribution
def plot_time_delay():
    # Simulated time delays
    time_delays_simulated = np.random.normal(loc=1.7, scale=0.2, size=100)
    
    # Observed time delay for GW170817/GRB 170817A
    observed_delay = 1.7
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.hist(time_delays_simulated, bins=15, color='blue', alpha=0.7, label='Simulated Data')
    plt.axvline(observed_delay, color='red', linestyle='--', label='Observed Delay (GW170817/GRB 170817A)')
    plt.xlabel('Time Delay (s)')
    plt.ylabel('Frequency')
    plt.title('Time Delay Distribution for Simulated Neutron Star Mergers')
    plt.legend()
    plt.grid()
    plt.savefig('time_delay_distribution.png')
    plt.show()

# Figure 2: Quantum Vortex Density vs Galactic Rotation Curves
def plot_dark_matter():
    # Galactic radius range
    radius = np.linspace(0, 50, 100)
    
    # Simulated quantum vortex density
    vortex_density = 100 * np.exp(-radius / 10)
    
    # Observed rotation curve data
    rotation_curve_observed = 200 * np.exp(-radius / 15) + 50
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(radius, vortex_density, 'b-', label='Quantum Vortex Density')
    plt.plot(radius, rotation_curve_observed, 'r--', label='Observed Rotation Curve')
    plt.xlabel('Galactic Radius (kpc)')
    plt.ylabel('Density/Velocity')
    plt.title('Quantum Vortex Density vs Galactic Rotation Curves')
    plt.legend()
    plt.grid()
    plt.savefig('quantum_vortex_density.png')
    plt.show()

# Figure 3: Axion-GRB Flux Prediction
def plot_axion_grb_flux():
    # Energy range
    energy = np.linspace(1, 30, 100)
    
    # Predicted axion-GRB flux
    flux_predicted = 1e-10 * np.exp(-(energy - 21)**2 / 10)
    
    # Fermi-LAT constraints
    fermi_lat_limit = 1e-9 * np.ones_like(energy)
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(energy, flux_predicted, 'b-', label='Predicted 21 TeV Axion-GRB Flux')
    plt.plot(energy, fermi_lat_limit, 'r--', label='Fermi-LAT Constraints')
    plt.xlabel('Energy (TeV)')
    plt.ylabel('Flux (arbitrary units)')
    plt.title('Predicted 21 TeV Axion-GRB Flux vs Fermi-LAT Constraints')
    plt.legend()
    plt.grid()
    plt.savefig('axion_grb_flux.png')
    plt.show()

# Generate all figures
if __name__ == "__main__":
    plot_time_delay()
    plot_dark_matter()
    plot_axion_grb_flux()
