# C(n, k) = C(n-1, k-1) + C(n-1, k)

"""
choosing k subset out of K
"""
def choose_subset(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return choose_subset(n-1, k-1) + choose_subset(n-1, k)

print(choose_subset(10, 3))