# Prompt: Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum. 

def squares(x):
    sum = 0
    sumsquares = 0
    for i in range(1, x + 1):
        sumsquares += i**2
        sum += i
    print((sum**2) - sumsquares)

squares(100)