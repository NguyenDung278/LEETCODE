class Solution:
    def findMaxConsecutiveOnes(self, nums) -> int:
        ans,check = 0,0
        for i in range(len(nums)):
            if nums[i]==1:
                check+=1
            else:
                ans = max(ans,check)
                check=0
        return max(ans,check)