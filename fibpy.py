
def fibp(n):
    a = 0 
    b = 1
    while b < n:
        a, b = b, a+b
        yield b

from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
import math 
  
# A function to print all prime factors of  
# a given number n 
def prime_factors(n): 
    fs = []
    while n % 2 == 0: 
        fs.append(2) 
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
        while n % i== 0: 
            fs.append(i)
            n = n / i 
              
    if n > 2: 
        fs.append(i)
    return sorted(list(fs))


def prime_factors_SA(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors




def iterncr(n):
    """
    def ncr(n, r):
    n / (n - r)!
    :param n:
    :return:
    """
    curr = 1
    prev = [1]
    while curr < n:
        arr = [1]
        for i in range(1, curr):
            arr.append(prev[i-1] + prev[i])
        prev = arr
    return prev

math.factorial(5)


import os
import sys

# Complete the solve function below.
def binomial(n):
    prev = []
    res = 1
    for r in range(1, n+2):
        prev.append(res)
        res = res * (n + 1 - r ) // r 
    return [x % (10**9) for x in prev ]

# Complete the solve function below.
def ncr_series(n):
    prev = []
    res = 1
    for r in range(1, n+2):
        prev.append(res)
        res = res * (n + 1 - r ) // r 
    return prev

def fastEXP(base, exp, modulus):
    base %= modulus
    result = 1
    while exp > 0:
        if exp & 1:
            result = (result * base) % modulus
        base = (base*base)%modulus
        exp >>= 1
    return result

def expt_bin_rl(a, b):
    r = 1
    while 1:
        if b % 2 == 1:
            r *= a
        b /= 2
        if b == 0:
            break
        a *= a
    return r