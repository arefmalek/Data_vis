import numpy as np
import matplotlib.pyplot as plt

import math

def polar(primes, limit):
    
    title = "Primes_under_{0}".format(limit)
    print(title)

    plt.title("Primes under {0}".format(limit))

    plt.subplot(1, 2, 1, projection = "polar")

    plt.polar(np.arange(limit), np.arange(limit), "g.", 
    markersize = 5/math.log10(limit))
    plt.xlabel("Regular")
    
    plt.subplot(1, 2, 2, projection = "polar")
    plt.polar(primes, primes, "r.", 
    markersize = 5/math.log10(limit))
    plt.xlabel('Primes')
   
    plt.show()

    # filename = "PrimeNumberPlot/primes_under_{total}.jpg".format(total = n)
    # plt.savefig(filename)   





def sieve(limit):
    answer = []
    plist = [True] * limit
    for i in range(2, limit):
        if plist[i]:
            answer.append(i)
            for j in range(i*i, limit, i):
                plist[j] = False
    
    polar(answer, limit)



n = 1_000
sieve(n)