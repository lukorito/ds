# Given a set of numbers and a target, find if there is a set of number adding up to the target

s = [1,2,3,4,5,6,7]
t = 20

def main(s,t):
    sorted = s.sort()
    nums = []
    while len(s) > 0:
        last_item = s.pop()
        nums.append(last_item)
        addition = sum(nums)
        if addition > t:
            nums.pop()
        if addition == t:
            return nums

print(main(s,t))