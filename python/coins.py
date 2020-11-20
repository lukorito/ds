# def change(amount):
#     assert(amount >=8)
#     if amount == 8:
#         return [3,5]
#     elif amount == 9:
#         retun [3,3,3]
#     elif amount === 10:
#         return [5,5]
    
#     coins = change(amount -3)
#     coins.append(3)
#     return coins

# 5 and 7 coins
# Question 1
# Imagine we have only 5- and 7-coins. One can prove that any large enough integer amount can be paid using only such coins. Yet clearly we cannot pay any of numbers 1, 2, 3, 4, 6, 8, 9 with our coins. What is the maximum amount that cannot be paid?
# N = xy - x - y

def change(amount):
    assert(amount>=24)
    if amount == 24:
        return [5,5,7,7]
    elif amount == 25:
        return [5,5,5,5,5]
    elif amount == 26:
        return [5, 7, 7, 7]
    elif amount == 27:
        return [5, 5, 5, 5, 7]        
    elif amount == 28:
        return [7,7,7,7]

    coins = change(amount - 5)
    coins.append(5)
    return coins
        

print(change(999))
    