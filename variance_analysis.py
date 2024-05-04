import utilities
import models
from numpy import array, sqrt, var, mean

def var_analysis(sigma, L: list):
    var_l = var(array(L))
    alpha1 = sqrt((var_l-sigma)/2)
    beta1 = mean(array(L)) - 4*alpha1
    H1 = []
    IH1 = []
    for l in L:
        H1.append((l-beta1)/alpha1)
    return H1  #H1 for the real values


