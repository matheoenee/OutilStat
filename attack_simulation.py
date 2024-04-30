from utilities import *
from models import Models
import random
import numpy as np

# inputs :
#   method (0 = slice, 1 = space)
#   loop (number of attack)
#   n (number of samples)
#   sigma (standard deviation)
#   Models (theorical models)
# output :
#   average key rank

def attack_simulation(method, loop, n, sigma, Models):
    kr_sum = 0 # sum of key rank
    for i in range(loop):

        k = random.randint(0, 255) # random key generation
        sigma_m = sigma
        sigma_y = sigma
        lm, ly = generate_leakages(n, sigma_m, sigma_y, k)

        # space method
        if method == 0:
            hm = space_method(lm)
            hy = space_method(ly)
        # slice method
        else:
            hm = slice_method(lm,n)
            hy = slice_method(ly,n)

        # generating empirical distribution D
        D = np.zeros((9, 9),dtype=int)
        for j in range(n):
            # Space method
            HWm = hm[j]
            HWy = hy[j]
            D[HWm][HWy] += 1
        D = D.astype(float)
        D /= n

        # get key rank
        kr = get_key_rank(Models,D,k)
        kr_sum += kr
    return kr_sum/loop
