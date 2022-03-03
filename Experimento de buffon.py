#Experimento de buffon
from cmath import pi
import random
import numpy as np
def buffon(N,l,d): #l=longitud del alfiler, d=distancia entre las rectas
    n = 0
    x = np.random.uniform(0,np.pi,N)
    theta = np.random.uniform(0,d/2,N)
    for i in range(N):
        if theta <= l * np.sin(x)/2:
            k = k + 1
    pi = (2 * l * N) /(d * k)
    return pi
