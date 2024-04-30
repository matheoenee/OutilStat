import random
import math
import matplotlib.pyplot as plt
import numpy as np

from utilities import *
from models import *
from attack_simulation import *

if __name__ == "__main__":
    sigma_value = [0.5,0.7,1,1.5]
    results = {}
    for sigma in sigma_value:
        results[sigma] = []
        results[sigma].append(128)
        print(f"[sigma = {sigma}]")
        for n in range(256, 4097, 256):
            average_kr = attack_simulation(1, 1000, n, sigma, Models)
            results[sigma].append(average_kr)
    
    # Tracer les résultats
    plt.figure(figsize=(10, 6))

    for sigma, values in results.items():
        plt.plot(range(0, 4097, 256), values, label=f"sigma = {sigma}")

    plt.xlabel('Number of observations')
    plt.ylabel('Correcte key rank')
    plt.legend(loc='upper right')  # Légende en haut à droite
    plt.xticks(np.arange(0, 4001, 500))  # Axe x de 0 à 4000 par pas de 500
    plt.yticks(np.arange(0, 141, 20))  # Axe y de 0 à 140 par pas de 20
    plt.xlim(0, 4000)  # Limite de l'axe x de 0 à 4000
    plt.ylim(0, 140)   # Limite de l'axe y de 0 à 140
    plt.grid(False)
    plt.show()