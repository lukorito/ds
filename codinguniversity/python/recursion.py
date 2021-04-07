import math

'''
 raising base^exp
 implementing using iterative solution
'''
def raise_iterative(base, exp):
    result = 1
    for i in range(exp):
        result *= base
    return result

# print(raise_iterative(5, 2))

'''
 raising base^exp
 implementing using recursion
'''

def raise_resursive(base, exp):
    if exp == 0:
        return 1
    else: 
        return base * raise_resursive(base, exp - 1)

# print(raise_resursive(100400, 200))

def efficient_raise(base, exp):
    if exp == 0:
        return 1
    else:
        half = efficient_raise(base, exp/2)
        if exp % 2 == 0:
            return half * half
        else:
            return base * half * half

# print(efficient_raise(5, 20))

def is_palindrome(s):
    # empty string is a palindrome
    if len(s) <= 1:
        return True
    return s[0].lower() == s[len(s) -1].lower() and is_palindrome(s[1: len(s) - 2])

# print(is_palindrome('Anna'))

def binary_search(arr, target):
    # use start and stop pointers
    def search(arr, start, stop, key):
        if start > stop:
            return
        mid = math.floor((stop - start) / 2)
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            search(arr, start, mid-1, key)
        else:
            search(arr, mid+1, stop, key) 

    return search(arr, 0, len(arr) - 1, target)
    

print(binary_search([1,2,3,4,5,6,7,8,50], 50))