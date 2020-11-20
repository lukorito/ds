# it is possible for n numbers
# we use recursion
# Solution: Move n-1 recursively
# It is possible for 1 and n-1
# Induction - prooving someting Recursion - Implementing something

moves = 0
def solve_hanoi(n,source,target,spare):
    global moves
    moves = moves + 1
        solve_hanoi(n-1, source, spare, target)
        target.append(source.pop())
        solve_hanoi(n-1, spare, target, source)
    return moves
    
    
    
    # https://blossoms.mit.edu/videos/lessons/towers_hanoi_experiential_recursive_thinking

A = [5,4,3,2,1]
B = []
C = []
print(solve_hanoi(5,A,B,C))