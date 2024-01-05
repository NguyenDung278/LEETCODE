class Solution:
    def containsDuplicate(self, nums) -> bool:
        dic = {}
        for c in nums:
            if c in dic:
                return True
            else:
                dic[c]=1
        return False

S = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
print(S.containsDuplicate(nums))
