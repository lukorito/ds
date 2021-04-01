import math

def binary_search(arr, target):
    mid = math.floor((len(arr) - 1) / 2)
    if arr[mid] > target:
        return binary_search(arr[0:mid], target)
    if arr[mid] < target:
        return binary_search(arr[mid:], target)
    if arr[mid] == target:
        return mid

print(binary_search([1,2,3,4,5,6,7,8,9], 4))
