#Generador de una distribución normal
from random import random
import matplotlib.pyplot as plt
def normal(mu,s):
    suma=0
    l=[]
    for i in range(12):
        suma=suma+random()
        x=mu + s * (suma - 6)
    return x 
l1=[]
for i in range(1000):
    l1.append(normal(180,15))
print(l1, len(l1))
plt.hist(l1, color='grey', edgecolor='black')
plt.xlabel('X generados')
plt.ylabel('Frecuencia')
plt.title('Histograma con 1000 números')
plt.show()