sum = 2
i = 1
j = 2
below = True

while below:
    i =  i + j
    j = j + i

    if i > 4000000 or j > 4000000:
        below = False
        continue

    if i % 2 == 0:
        sum += i
    if j % 2 == 0:
        sum += j

print(sum)