# generate permutations
def can_be_extended(perm):
    i = len(perm) - 1
    for j in range(i):
        if i - j == abs(perm[i] - perm[j]):
            return False
    return True

count = 0
def extends(perm, n):
    if len(perm) == n:
        print(perm)
        global count
        count = count+ 1
        # exit()

    for k in range(n):
        if k not in perm:
            perm.append(k)
            if can_be_extended(perm):
                extends(perm, n)
            perm.pop()

extends(perm=[], n=8)
print(count)