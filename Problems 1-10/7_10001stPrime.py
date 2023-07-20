# Prompt: What is the 10001st prime number?

import time
starttime = time.time()

primes = []

def isPrime(n):
    for i in range(2, int(n**0.5) + 1):
        # goes through every number up til the root of the number being checked
        if n % i == 0:
            # if no remainder, then it is not prime
            return False
    return True

i = 2

while len(primes) < 10001:
    if isPrime(i):
        primes.append(i)
    i += 1

print(primes[10000])
print(time.time() - starttime)