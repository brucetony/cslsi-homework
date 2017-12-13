# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 14:44:21 2017

@author: Bruce
"""
def sieve(n):
    """Uses Sieve of Eratosthenes algorith to compute \
    list of prime numbers up to the given number"""
    if n<=1:
        raise Exception('Input number must be greater than 1!')
    primes=[]
    multiples=[]
    for probe in range(2, n+1): #Need to add 1 to include input number in calc
        if probe not in multiples:
            primes.append(probe)
            p=2
            while (p*probe<=n+1):
                multiples.append(p*probe)
                p+=1
    return primes
    

def sieve2(n):
    primes=[]
    multiples=[]
    probe=2
    while probe<=n:
        while (probe not in multiples) and (probe not in primes):
            primes.append(probe)
            p=1
            while (p*probe<=n+1):
                multiples.append(p*probe)
                p+=1
        probe+=1
    return primes

def sieve3(n):
    primes=[]
    multiples=[]
    for probe in range(2, n+1): #Need to add 1 to include input number in calc
        if probe in multiples or probe in primes:
            pass
        else:
            primes.append(probe)
            p=1
            while (p*probe<=n+1):
                multiples.append(p*probe)
                p+=1
    return primes

def sieve4(n):
    """Uses Sieve of Eratosthenes algorith to compute \
    list of prime numbers up to the given number"""
    if n<=1:
        raise Exception('Input number must be greater than 1!')
    primes=[]
    multiples=[]
    for probe in range(2, n+1): #Need to add 1 to include input number in calc
        if probe not in multiples:
            primes.append(probe)
            for p in range(probe*probe, n+1, probe):
                multiples.append(p)
    return primes
    

import time
start_time = time.time()
sieve4(100000)
print("--- %s seconds ---" % (time.time() - start_time))