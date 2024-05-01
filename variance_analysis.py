import utilities
import models
from numpy import array, sqrt, var, mean

def var_analysis(sigma, L: list):
    var_l = var(array(L))
    alpha1 = sqrt((var_l-sigma)/2)
    alpha2 = -alpha1
    beta1 = mean(array(L)) - 4*alpha1
    beta2 = mean(array(L)) - 4*alpha2
    print(f"alp1 = {alpha1}, alp2 = {alpha2}, beta1 = {beta1}, beta2 = {beta2}")
    H1, H2 = [], []
    for l in L:
        H1.append((l-beta1)/alpha1)
        H2.append((l-beta2)/beta2)
    return H1, H2