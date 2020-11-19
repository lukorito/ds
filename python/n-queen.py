import itertools as it

def is_solution(perm):
    for (l1, l2) in it.combinations(range(len(perm)), 2):
        if abs(l1 - l2) == abs(perm[l1] - perm[l2]):
            return False
    
    return True

for perm in it.permutations(range(20)):
    if is_solution(perm):
        print(perm)
        exit()

