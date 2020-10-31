import numpy as np
import matplotlib.pyplot as plt

def polar(primes):
    plt.polar(primes, primes, "ro")
    plt.ylabel('primes')
    plt.show()

def sieve(number):
    answer = []
    plist = [True] * number
    for i in range(2, number):
        if plist[i]:
            answer.append(i)
            for j in range(i*i, number, i):
                plist[j] = False
    
    polar(answer)

def regular(number):
    polar(np.arange(number))


n = 1_000

