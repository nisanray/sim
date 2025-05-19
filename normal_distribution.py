import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

def normal_simulation(mean, std_dev, sample_size):
    data = np.random.normal(loc=mean, scale=std_dev, size=sample_size)
    print(f"\n--- Normal Distribution Simulation ---")
    print(f"Mean: {mean}, Std Dev: {std_dev}, Sample Size: {sample_size}")
    
    # Histogram
    plt.hist(data, bins=30, density=True, edgecolor='black', alpha=0.6)

    # Plot theoretical PDF
    x = np.linspace(min(data), max(data), 100)
    plt.plot(x, norm.pdf(x, mean, std_dev), 'r', lw=2, label='PDF')
    plt.title(f'Normal Distribution N({mean}, {std_dev}²)')
    plt.xlabel('Value')
    plt.ylabel('Density')
    plt.grid(True)
    plt.legend()
    plt.show()

# 📥 User Input
try:
    mean = float(input("Enter mean (μ): "))
    std_dev = float(input("Enter standard deviation (σ): "))
    sample_size = int(input("Enter sample size: "))
    normal_simulation(mean, std_dev, sample_size)
except ValueError as e:
    print("Invalid input:", e)
