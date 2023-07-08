# Prompt: The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143?

primes = []
y = 2
primefound = False

def primefactor(x):
    # recursively divides input by prime factor until input = 1 
    if x != 1:
        for i in range(2, x + 1):
            if x % i == 0:
                # if x is divisible by 1, the remainder will be 0
                primes.append(i)
                x = int(x/i)
                primefactor(x)
                return
    else:
        return

primefactor(600851475143)
print(primes)
