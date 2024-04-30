import numpy as np
import random

from utilities import hw, SBOX

Models = []
for k in range(256):
    Mk = np.zeros((9, 9), dtype=int)
    for m in range(256):
        hm = hw[m]
        hy = hw[int(SBOX[k ^ m])]
        Mk[hm][hy] += 1
    Mk = Mk.astype(float)  # float conversion
    Mk /= 256
    Models.append(Mk)