from utilities import *
import random
import numpy as np

# inputs :
#   conversion method (0 = slice, 1 = space, 2 = variance analysis)
#   attack (0 = classical CPA, 1 = ML criterion)
#   loop (number of attack)
#   n (number of samples)
#   sigma (standard deviation)
#   Models (theorical models)
# output :
#   average key rank

def attack_simulation(method, attack, loop, n, sigma, Models):
    kr_sum = 0 # sum of key rank
    for i in range(loop):

        # leakage simulation 
        k = random.randint(0, 255) # random key generation
        print("k = ",k)
        sigma_m = sigma
        sigma_y = sigma
        lm, ly = generate_leakages(n, sigma_m, sigma_y, k)
        
        # leakage conversion into HW
        if method == 0: # space method
            hm = space_method(lm)
            hy = space_method(ly)
        elif method == 1: # slice method
            hm = slice_method(lm)
            hy = slice_method(ly)
        elif method == 2: # variance anlysis
            hm = var_analysis(sigma_m, lm) 
            hy = var_analysis(sigma_y, ly)

        # attack simulation 
        if attack == 0: # classical CPA
            sorted_dict = classical_CPA(hm, hy, n)
        elif attack == 1: # ML criterion
            sorted_dict = ML_criterion(hm, hy, sigma_m, sigma_y, n)

        print(sorted_dict)

        kr = get_key_rank(sorted_dict, k)
        print(f"[{i}] kr = {kr}")
        kr_sum += kr

    return kr_sum/loop
