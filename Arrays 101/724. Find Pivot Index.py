class Solution:
    def pivotIndex(self, nums) -> int:
        S = sum(nums)
        sumleft = 0
        for i,x in enumerate(nums):
            if sumleft == (S-x-sumleft):
                return i
            sumleft+=nums[i]
        return -1