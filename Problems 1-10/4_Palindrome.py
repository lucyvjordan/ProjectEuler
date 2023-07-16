""" Prompt: A palindromic number reads the same both ways. The largest palindrome made from the product of two 
2-digit numbers is 9009 = 91 x 99. Find the largest palindrome made from the product of two 3-digit numbers. """

largest = 0
palin = False

for i in range (100, 1000):
    for j in range (100, 1000):
        palin = True
        num = i*j
        numstring = str(num)
        
        for k in range(0, len(numstring)):
            # goes through the length of the string and checks if its a palindrome
            if numstring[k] == numstring[-(k+1)]:
                # if the letter at the reverse index of k is the same as k, it suits the conditions of a palindrome
                pass
            else:
                palin = False
                break

        if palin == True:
            if num > largest:
                largest = num
                
print(largest)

                
                        
