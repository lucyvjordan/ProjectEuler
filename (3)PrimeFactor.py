primes = []
y = 2
primefound = False
def primefactor(x):
    if x != 1:
        for i in range(2,x + 1):
            print(x,i)
            if x % i == 0:
                primes.append(i)
                x = int(x/i)
                primefactor(x)
                return
    else:
        return


primefactor(600851475143)
print(primes)


