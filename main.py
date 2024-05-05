import random
import math
import matplotlib.pyplot as plt
import numpy as np
from utilities import *
#from models import *
from attack_simulation import *

if __name__ == "__main__":
    average_kr = attack_simulation(0, 1, 1, 512, 0.5, Models)
    """
    sigma_value = [0.5, 0.7, 1, 1.5]
    results = {}
    for sigma in sigma_value:
        results[sigma] = []
        results[sigma].append(128)
        print(f"[sigma = {sigma}]")
        for n in range(256, 4097, 256):
            average_kr = attack_simulation(1, 1000, n, sigma, Models)
            print(f"    [n = {n}] average key rank is : ", average_kr)
    """
    
    
    