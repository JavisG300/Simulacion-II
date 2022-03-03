#Experimento de buffon
import numpy as np
def buffon(N,l,d): #l=longitud del alfiler, d=distancia entre las rectas
    n = 0
    x = np.random.uniform(0,np.pi,N)
    theta = np.random.uniform(0,d/2,N)
    for i in range(N):
        if theta <= l * (np.sin(x)/2):
            n = n + 1
    pi = (2*l*N) /(d*n)
    return pi
print(buffon(100,0.8,1))