import numpy as np
import matplotlib.pyplot as plt

def plot_quantum_decoherence_rates():
    # System size range
    system_size = np.linspace(1, 100, 100)
    
    # Observed decoherence rates (decreasing trend)
    decoherence_obs = 1e-3 * np.exp(-system_size / 50) + 1e-5 * np.random.normal(size=len(system_size))
    
    # Revised predictions (gravitationally suppressed decoherence)
    decoherence_pred = 1e-3 * np.exp(-system_size / 50) * (1 - 0.05 * np.sqrt(system_size))
    
    # Plot
    plt.figure(figsize=(10, 6))
    plt.plot(system_size, decoherence_obs, 'bo', label='Observed Data')
    plt.plot(system_size, decoherence_pred, 'r-', label='Revised Prediction')
    plt.xlabel('System Size (Arbitrary Units)')
    plt.ylabel('Decoherence Rate')
    plt.title('Quantum Decoherence Rates')
    plt.legend()
    plt.grid()
    plt.savefig('quantum_coherence_observed_vs_model.png')
    plt.show()

# Generate the figure
if __name__ == "__main__":
    plot_quantum_decoherence_rates()
