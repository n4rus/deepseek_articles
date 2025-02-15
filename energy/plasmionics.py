import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn')

# Figure 1: Plasma Emission vs. PV/TPV Response
def plot_spectra():
    wavelength = np.linspace(200, 2000, 1000)  # nm
    plasma_emission = 1e4 * np.exp(-(wavelength - 500)**2 / (2*100**2))  # Argon plasma peak at 500 nm
    tpv_response = np.where((wavelength > 1500) & (wavelength < 2000), 0.8, 0)  # GaSb TPV
    pv_response = np.where((wavelength > 300) & (wavelength < 800), 0.6, 0)  # SiC PV
    
    plt.figure(figsize=(10,6))
    plt.plot(wavelength, plasma_emission, label='Plasma Emission (Argon)')
    plt.plot(wavelength, tpv_response, label='TPV Response (GaSb)')
    plt.plot(wavelength, pv_response, label='PV Response (SiC)')
    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Normalized Intensity/Efficiency')
    plt.legend()
    plt.savefig('spectra.png')

# Figure 2: TPV Efficiency vs. Temperature
def plot_efficiency():
    temp = np.linspace(800, 1500, 100)
    efficiency = 0.3 * (1 - np.exp(-(temp - 800)/200))  # Empirical model
    
    plt.figure(figsize=(10,6))
    plt.plot(temp, efficiency*100, 'r-')
    plt.xlabel('Emitter Temperature (°C)')
    plt.ylabel('TPV Efficiency (%)')
    plt.savefig('efficiency.png')

# Figure 3: Hybrid System Efficiency
def plot_hybrid():
    stages = ['Thermionics', 'TPV', 'Turbine', 'Total']
    efficiency = [15, 25, 30, 55]
    
    plt.figure(figsize=(10,6))
    plt.bar(stages, efficiency, color=['blue', 'orange', 'green', 'red'])
    plt.ylabel('Efficiency (%)')
    plt.ylim(0, 60)
    plt.savefig('hybrid.png')

if __name__ == "__main__":
    plot_spectra()
    plot_efficiency()
    plot_hybrid()
