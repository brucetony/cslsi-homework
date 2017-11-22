
"""
@author: Bruce Schultz
@author_email: bschultz@uni-bonn.de

"""
#Exercise 01
def pascal(rowN, outputPath):
    """Enter desired row number of pascal triangle and it will print\
    all rows for you"""
    if rowN < 0:
        raise Exception("You cannot enter a negative row number!")
    elif rowN == 0:
        return [1]
    else:
        try:
            result=[[1]]
            for n in range(1, rowN+1):
                result.append([1])
                for k in range(n-1):
                     next_value = result[n-1][k] + result[n-1][k+1]
                     result[n].append(next_value)
                result[n].append(1)
            with open(outputPath, 'w') as output:
                max_width = len(' '.join(map(str,result[-1])))
                for row in result:
                    output.write(' '.join(map(str,row)).center(max_width)+'\n')
        except FileNotFoundError:
            print('Please check if output path is valid.')

#Exercise 02
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
    
def factorize(m):
    """Uses sieve() to factor a given number m using prime numbers \
    until it has been reduced to a prime number, then returns \
    the factors and powers in dict"""
    primes = sieve(m)
    #primes = primes[::-1]
    factors=[]
    i=0
    while m not in primes and m >= 2:
        while m % primes[i] == 0:
            factors.append(primes[i])
            m = m/primes[i]
        i+=1
    if m != 1: #Must be included to avoid having 1 added to dict
        factors.append(int(m))
    powers=[]
    unique_factors=[]
    for value in factors:
        if value not in unique_factors:
            unique_factors.append(value)
            powers.append(factors.count(value))
    factor_dict=dict(zip(unique_factors, powers))
    return factor_dict


print(factorize(123464))