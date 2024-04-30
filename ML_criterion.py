from random import random, randint
from utilities import *
from numpy import sqrt, pi, exp
from models import Models


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
        hh_prob = k_model[hh[0], hh[1]]  #P((hh_m,hh_y)|k) NEED TO BE COMPUTE !
        prob_h_hh = prob_noise(sigma_m, sigma_y, h, hh)
        S += prob_h_hh * hh_prob
    return S

def prob_k(h, k, sigma_m, sigma_y, P_k):
    """
    Avec la formule des probabilités totales, on peut obtenir P(h) en calculant la somme des P(h*)P(h|h*)
    Or P(h|h*) est déjà calculé pour la proba du bruit.
    """
    P_h = 1  #0
    """for hh in couples_weight:
        P_h += 1/81 * prob_noise(sigma_m, sigma_y, h, hh)  # not sure about that"""
    return (total_prob(h, k, sigma_m, sigma_y) * P_k / P_h)


### starts program
K = randint(1, 255)

N = 256

sigma_m = 1.5
sigma_y = 1.5

hm, hy = generate_leakages(N, sigma_m, sigma_y, K)
H = [(hm[i], hy[i]) for i in range(N)]

PROB_k = [1/256 for i in range(256)]  #probabilities of each key, initialized to uniform distribution P(k)

for h in H:
    for k in range(256):
        PROB_k[k] = prob_k(h, k, sigma_m, sigma_y, PROB_k[k])

k = PROB_k.index(max(PROB_k))
print(k)
print(PROB_k)
print(K)