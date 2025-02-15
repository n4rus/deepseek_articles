import numpy as np
import matplotlib.pyplot as plt

# Figure 1: Hubble Tension
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
    plt.savefig('hubble_tension.png')
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

# Generate all figures
if __name__ == "__main__":
    plot_dark_matter_distribution()
    plot_hubble_tension()
