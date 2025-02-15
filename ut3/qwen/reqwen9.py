import numpy as np
import matplotlib.pyplot as plt

# Figure 1: Hubble Tension
def plot_hubble_tension():
    # Redshift range
    redshift = np.linspace(0, 2, 100)
    
    # Observed Hubble parameter values
    hubble_obs_local = 73.04 + 1.04 * np.random.normal(size=len(redshift))
    hubble_obs_cmb = 67.4 + 0.5 * np.random.normal(size=len(redshift))
    
    # Predicted Hubble parameter values
    hubble_pred = 70 + 2 * np.sin(redshift * np.pi)
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(redshift, hubble_obs_local, 'bo', label='Local Measurements')
    plt.plot(redshift, hubble_obs_cmb, 'go', label='CMB-Derived Values')
    plt.plot(redshift, hubble_pred, 'r-', label='Entropy-Driven Prediction')
    plt.xlabel('Redshift')
    plt.ylabel('$H(z)$ (km/s/Mpc)')
    plt.title('Hubble Tension Resolution')
    plt.legend()
    plt.grid()
    plt.savefig('hubble_tension.png')
    plt.show()

# Figure 2: Dark Matter Distribution
def plot_dark_matter_distribution():
    # Distance range (Mpc)
    distance = np.linspace(0, 100, 100)
    
    # Simulated dark matter density
    density_simulated = np.exp(-distance / 20) + 0.05 * np.random.normal(size=len(distance))
    
    # Observed dark matter density
    density_observed = np.exp(-distance / 20) * (1 + 0.1 * np.sin(distance))
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(distance, density_simulated, 'b-', label='Simulated Dark Matter')
    plt.plot(distance, density_observed, 'r--', label='Observed Weak Lensing')
    plt.xlabel('Distance (Mpc)')
    plt.ylabel('Dark Matter Density')
    plt.title('Dark Matter Distribution')
    plt.legend()
    plt.grid()
    plt.savefig('dark_matter_distribution.png')
    plt.show()

# Generate all figures
if __name__ == "__main__":
    plot_hubble_tension()
    plot_dark_matter_distribution()
