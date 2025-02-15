import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Wedge

plt.style.use('seaborn-whitegrid')
plt.rcParams.update({
    "font.family": "serif",
    "font.size": 12,
    "axes.titlesize": 14,
    "axes.labelsize": 12
})

def plot_system_schematic():
    fig, ax = plt.subplots(figsize=(10, 8))
    
    # Core components
    ax.add_patch(Rectangle((0.3, 0.4), 0.4, 0.4, fc='lightcoral', ec='firebrick'))
    ax.text(0.5, 0.6, "Plasma Core\n(10$^4$ K)", ha='center', va='center')
    
    # Magnets
    ax.add_patch(Wedge((0.2, 0.5), 0.15, 270, 90, fc='skyblue', ec='navy'))
    ax.text(0.2, 0.65, "HTS Magnets\n(20 K)", ha='center')
    
    # Divertor
    ax.add_patch(Rectangle((0.3, 0.3), 0.4, 0.05, fc='gold', ec='darkorange'))
    ax.text(0.5, 0.325, "Thermionic Divertor", ha='center')
    
    # Turbine
    ax.plot([0.7, 0.9], [0.5, 0.5], lw=2, color='green')
    ax.add_patch(Rectangle((0.85, 0.45), 0.1, 0.1, fc='lightgreen', ec='darkgreen'))
    ax.text(0.9, 0.5, "Cryo Turbine", ha='center', va='center')
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    plt.savefig('system_schematic.pdf', bbox_inches='tight')

def plot_spectral_response():
    wavelength = np.linspace(200, 2500, 1000)
    plasma = 1e4 * np.exp(-(wavelength - 500)**2/(2*100**2)) + \
            0.5e4 * np.exp(-(wavelength - 1500)**2/(2*300**2))
    
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(wavelength, plasma, label='Plasma Emission (Ar/Ne)')
    ax.fill_between(wavelength, 0, np.where((wavelength>300)&(wavelength<800), 0.8, 0),
                    alpha=0.3, label='SiC PV Response')
    ax.fill_between(wavelength, 0, np.where((wavelength>1500)&(wavelength<2500), 0.6, 0),
                    alpha=0.3, label='GaSb TPV Response')
    
    ax.set(xlim=(200, 2000), xlabel='Wavelength (nm)',
           ylabel='Normalized Intensity/Response',
           title='Spectral Matching')
    ax.legend()
    plt.savefig('spectral_response.pdf', bbox_inches='tight')

def plot_efficiency_breakdown():
    components = ['Thermionics', 'TPV', 'Turbine', 'Ambient']
    efficiency = [15, 25, 30, 0.5]
    
    fig, ax = plt.subplots(figsize=(8, 5))
    bars = ax.bar(components, efficiency, color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728'])
    
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{height}%', ha='center', va='bottom')
    
    ax.set_ylim(0, 35)
    ax.set_ylabel('Efficiency (%)')
    ax.set_title('Energy Conversion Efficiency Breakdown')
    plt.savefig('efficiency_breakdown.pdf', bbox_inches='tight')

def plot_validation_curves():
    models = ['Thermionic', 'TPV', 'Diode']
    simulation = [1.5, 27, 9.8]
    experiment = [1.2, 25, 8.5]
    error = [0.2, 1.5, 0.7]
    
    x = np.arange(len(models))
    fig, ax = plt.subplots(figsize=(8, 5))
    
    ax.errorbar(x, simulation, yerr=error, fmt='o', capsize=5,
                label='Simulation', markersize=8)
    ax.scatter(x, experiment, marker='s', s=80, label='Experimental Targets')
    
    for i, txt in enumerate(models):
        ax.text(x[i]-0.1, simulation[i]+0.5, txt)
    
    ax.set_xticks([])
    ax.set_ylabel('Normalized Performance')
    ax.set_title('Simulation vs Experimental Validation')
    ax.legend()
    plt.savefig('validation_curves.pdf', bbox_inches='tight')

if __name__ == "__main__":
    plot_system_schematic()
    plot_spectral_response()
    plot_efficiency_breakdown()
    plot_validation_curves()
    print("Figures generated: system_schematic.pdf, spectral_response.pdf, efficiency_breakdown.pdf, validation_curves.pdf")
