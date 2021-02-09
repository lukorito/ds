# Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        #use two pointer method to track items
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != nums[slow]:
                # swap
                slow+=1
                temp = nums[slow] # requires extra  memory [O(n)]
                nums[slow] = nums[fast]
                nums[fast] = temp
        # return slow + 1 for the last part
        return slow+1

