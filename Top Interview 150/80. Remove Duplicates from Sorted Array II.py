class Solution:
    def removeDuplicates(self, nums) -> int:
        length = 0
        for index,val in enumerate(nums):
            if (length<=1) or (nums[length-2] != val):
                nums[length] = val
                length+=1
        return length
    
