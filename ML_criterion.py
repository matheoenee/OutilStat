from random import random, randint
from utilities import *
from numpy import sqrt, pi, exp
from models import Models
from variance_analysis import var_analysis


def prob_noise(sigma_m, sigma_y, h: tuple, hh: tuple):
    exp_m = -1/2 * ((h[0]-hh[0])/sigma_m)**2
    exp_y = -1/2 * ((h[1]-hh[1])/sigma_m) ** 2

    Pm = 1/(sigma_m*sqrt(2*pi)) * exp(exp_m)
    Py = 1/(sigma_y*sqrt(2*pi)) * exp(exp_y)

    return Pm * Py

def total_prob(h, k, sigma_m, sigma_y):
    S = 0
    k_model = Models[k]
    for hh in couples_weight:
        hh_prob = k_model[hh[0], hh[1]]  #P((hh_m,hh_y)|k), precomputes in the models
        prob_h_hh = prob_noise(sigma_m, sigma_y, h, hh)
        S += prob_h_hh * hh_prob
    return S

def ML_criterion(hm, hy, sigma_m, sigma_y):
    H = [(hm[i], hy[i]) for i in range(N)]
    PROB_k = [1 / 256 for i in range(256)]  # probabilities of each key, initialized to uniform distribution P(k)
    i = 0
    for h in H:
        for k in range(256):
            PROB_k[k] *= total_prob(h, k, sigma_m, sigma_y) * N**(0.4672)  # for not extra divergence
        i += 1
        if i % 50 == 0:
            print(PROB_k)
    return PROB_k, PROB_k.index(max(PROB_k))


### starts program
K = randint(1, 255)

N = 2000

sigma_m = 0.5
sigma_y = 0.5

lm, ly = generate_leakages(N, sigma_m, sigma_y, K)
print("first step : variance analysis")
hm, hy = var_analysis(sigma_m, lm), var_analysis(sigma_y, ly)
print("DONE")
print("ML criterion method")
k = ML_criterion(hm, hy, sigma_m, sigma_y)
print("DONE\n\nresults :")
print(k[0])
print(f"key deduced by ML criterion: {k[1]}")
print(f"right key: {K}")