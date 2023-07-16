""" Prompt: 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 
 without any remainder.What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20. """

import time
starttime = time.time()

nums = [12, 14, 15, 16, 18, 20]

def smallest_multiple():
    i = 46189
    # 11 * 13 * 17 * 19 = 46189, so increase by 46189 each time instead of 1
    running = True
    while running:
        multiple = True

        for num in nums:
            if i % num == 0:
                pass
            else:
                multiple = False
                # if the number is not visible by one of the factors, it doesnt fit the criteria and so break to save time
                break

        if multiple == True:
            return i
            # return i if multiple is still True, as this means all the numbers are factors
        else:
            i += 46189

print(smallest_multiple())
print(time.time() - starttime)
