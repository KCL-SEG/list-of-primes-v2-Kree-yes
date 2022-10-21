"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):

    if (number_of_primes <= 0):
        raise ValueError("number of primes not positive")
    
    list = []
    currentNum = 2

    while number_of_primes > 0:
        if is_prime(currentNum):
            list.append(currentNum)
            number_of_primes -= 1
        
        currentNum += 1
        
    return list

def is_prime(number):
    divisors = 0

    for i in range(2, number+1):
        if (number % i) == 0:
            divisors += 1
    
    if divisors == 1:
        return True
    else:
        return False