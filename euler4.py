
#Function to determine if string is a palindrome
def isPalindrome(str):
    res = False
    half = len(str)/2
    for x in range(0, half):
        #compare the character from the index in the left from the one in the right of the string
        if str[x] == str[-x-1]:
            res = True
        else: #if false, then its not a palindrome. Break the loop
            res = False
            break
    return res

largest = 0
for i in range(100,1000):
    for j in range(100,1000):
        #product of two numbers
        prod = i * j
        prodStr = str(prod)
        # if it is a palindrome and is largest than the previous product stored, store as the larges
        if (isPalindrome(prodStr) and prod>largest):
            largest = prod

print(largest)
