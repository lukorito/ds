def set_bit(x, position):
    mask = 1 << position
    return x | mask

# print(bin(set_bit(0b00000110, 0)))

def clear_bit(x, position):
    mask = 1 << position
    return x & ~mask

# print(bin(clear_bit(0b00000111, 0)))

def flip_bit(x, position):
    mask = 1 << position
    return x ^ mask

# print(flip_bit(0b00000111, 4))

def is_bit_set(x, position):
    shifted = x >> position
    return shifted & 1 == 1

# print(is_bit_set(0b00000111, 2))
'''
Bit Tricks
'''
def is_even(x):
    return (x & 1) == 0

# print(is_even(401))

def is_power_of_two(x):
    # any number that is a power of two will have one binary set
    return (x & x - 1) == 0