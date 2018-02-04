
#Function to determine if string is a palindrome
def isPalindrome(str):
    res = False
    half = len(str)/2
    for x in range(0, half):
        if str[x] == str[-x-1]:
            res = True
        else:
            res = False
            break
    return res

largest = 0
for i in range(100,1000):
    for j in range(100,1000):
        #product of two numbers
        prod = i * j
        prodStr = str(prod)
        if (isPalindrome(prodStr) and prod>largest):
            largest = prod

print(largest)

# def totalPalindrome(min, max):
#     sum = 0
#     for x in range(min,max+1):
#         xStr = str(x)
#         # print('{} is palindrom: {}'.format(x, isPalindrome(xStr)))
#         if (isPalindrome(xStr)):
#             sum += x
#
#     return sum
