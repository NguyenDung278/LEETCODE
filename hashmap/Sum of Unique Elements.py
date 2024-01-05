from collections import Counter
class Solution:
    def sumOfUnique(self, nums) -> int:
        s= Counter(nums)
        sum = 0
        for c in nums:
            if s[c]==1:
                sum+=c
        return sum

S = Solution()
nums = [1,2,3,2]
print(S.sumOfUnique(nums))
