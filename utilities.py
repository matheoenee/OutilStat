import random
import math
import matplotlib.pyplot as plt
import numpy as np
from numpy import array, sqrt, var, mean
from numpy import sqrt, pi, exp

SBOX = [
   0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
   0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
   0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
   0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
   0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
   0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
   0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
   0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
   0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
   0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
   0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
   0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
   0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
   0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
   0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
   0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
]

invSBOX = [
	0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
	0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
	0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
	0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
	0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
	0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
	0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
	0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
	0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
	0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
	0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
	0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
	0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
	0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
	0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
	0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D
]

hw = [
  0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
  1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
  1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
  2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
  1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
  2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
  2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
  3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7, 4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 7, 6, 7, 7, 8
]

couples_weight = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8),
                  (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),
                  (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
                  (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8),
                  (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7), (4, 8),
                  (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8),
                  (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7), (6, 8),
                  (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8),
                  (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7), (8, 8)]

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

# function that generate electrical power
def generate_ep(a,b,sigma,hw):
    noise = random.gauss(0,sigma)
    return a*(hw + noise) + b

# function to compute distance between two statistical distributions
def distribution_distance(D1,D2):
        sum = 0
        for hm in range(9):
            for hy in range(9):
                sum += pow((D1[hm][hy] - D2[hm][hy]), 2)
        return math.sqrt(sum)

# function to print 3D representation of statistical distribution
def print_distribution(D):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x_data, y_data = np.meshgrid(np.arange(D.shape[1]),
                            np.arange(D.shape[0]))
    x_data = x_data.flatten()
    y_data = y_data.flatten()
    z_data = D.flatten()
    ax.bar3d( x_data,
          y_data,
          np.zeros(len(z_data)),
          1, 1, z_data )
    plt.show()

# function that generate leakage given n, sigma and key
def generate_leakages(n, sigma_m, sigma_y, k):
    am, bm = random.randint(5, 20), random.randint(0, 150) # parameters for message electric power
    ay, by = random.randint(5, 20), random.randint(0, 150) # parameters for ciphertext electric power

    lm = []
    ly = []
    # Hm = []
    # Hy = []
    for i in range(n):
        m = random.randint(0, 255) # random plaintext message
        hm = hw[m]  #haming weight of m
        hy = hw[int(SBOX[k^m])]  #haming weight of y
        # Hm.append(hm)
        # Hy.append(hy)

        # electric power simulation with noise
        ep_m = generate_ep(am, bm, sigma_m, hm)
        ep_y = generate_ep(ay, by, sigma_y, hy)

        lm.append(ep_m)
        ly.append(ep_y)
    return lm, ly  #, Hm, Hy

# function that convert leakage into HW by space methode
def space_method(leakage):
    b = [0,0,0,0,0,0,0,0,0]

    min_value = min(leakage)
    max_value = max(leakage)
    space = (max_value - min_value)/8

    b[0] = min_value + space/2
    for i in range(1,9):
        b[i] = b[i-1] + space

    HW = []
    for power in leakage:
        for i in range(9):
            if power < b[i]:
                HW.append(i)
                break
    return HW
    
# function that convert leakage into HW by slice method (Linge)
def slice_method(leakage):
    n = len(leakage)
    permutation = sorted(range(len(leakage)), key=lambda k: leakage[k])
    # Inverting the permutations
    inv_permutation = np.argsort(permutation)
    # Applying the permutation to sort the array
    sorted_leakage = np.array(leakage)[permutation]

    # Converting the array in HW with the slice method
    lower_bound = 0
    for h in range(9):
        upper_bound = lower_bound + int((math.comb(8, h)*n)/256)        
        sorted_leakage[lower_bound:upper_bound] = h
        sorted_leakage[lower_bound:upper_bound] = h
        lower_bound = upper_bound

    # Convert to integers
    converted_leakage = sorted_leakage.astype(int)
    # Applying the inverse permutation to return to the original state
    return converted_leakage[inv_permutation]

# function that convert leakage into real HW
def var_analysis(sigma, L: list):
    var_l = var(array(L))
    alpha1 = sqrt((var_l-sigma)/2)
    beta1 = mean(array(L)) - 4*alpha1
    H1 = []
    IH1 = []
    for l in L:
        H1.append((l-beta1)/alpha1)
    return H1  #H1 for the real values

# function that silmulate classical CPA attack, return list of key ordered by model distance
def classical_CPA(hm,hy,n):
    D = np.zeros((9, 9),dtype=int)
    for j in range(n):
        HWm = hm[j]
        HWy = hy[j]
        D[HWm][HWy] += 1
    D = D.astype(float)
    D /= n

    distance_dict = {}
    for key in range(256):
        distance_dict[key] = distribution_distance(Models[key], D)

    sorted_distance_dict = dict(sorted(distance_dict.items(), key=lambda item: item[1]))
    return sorted_distance_dict

# function that return the noise probability (used in ML criterion)
def prob_noise(sigma_m, sigma_y, h: tuple, hh: tuple):
    exp_m = -1/2 * ((h[0]-hh[0])/sigma_m)**2
    exp_y = -1/2 * ((h[1]-hh[1])/sigma_m) ** 2

    Pm = 1/(sigma_m*sqrt(2*pi)) * exp(exp_m)
    Py = 1/(sigma_y*sqrt(2*pi)) * exp(exp_y)

    return Pm * Py

# function that return the total probability (used in ML criterion)
def total_prob(h, k, sigma_m, sigma_y):
    S = 0
    k_model = Models[k]
    for hh in couples_weight:
        hh_prob = k_model[hh[0], hh[1]]  #P((hh_m,hh_y)|k), precomputes in the models
        prob_h_hh = prob_noise(sigma_m, sigma_y, h, hh)
        S += prob_h_hh * hh_prob
    return S

# function that simulate attack using ML criterion, return list of key ordered by probability
def ML_criterion(hm, hy, sigma_m, sigma_y, n):
    H = [(hm[i], hy[i]) for i in range(n)]
    prob_dict = {i: 1 / 256 for i in range(256)}  # probabilities of each key, initialized to uniform distribution P(k)
    for h in H:
        for k in range(256):
            prob_dict[k] *= total_prob(h, k, sigma_m, sigma_y) * n**(0.4672)  # for not extra divergence

    sorted_prob_dict = dict(sorted(prob_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_prob_dict

# function that return the key rank
def get_key_rank(sorted_dict,k):
    rank = None
    keys = list(sorted_dict.keys())
    if k in keys:
        rank = keys.index(k)
    return rank
