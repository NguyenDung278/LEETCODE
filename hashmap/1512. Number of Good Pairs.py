from collections import Counter
class Solution:
    def numIdenticalPairs(self, nums) -> int:
        d = Counter(nums)
        c = 0
        for i in d:
            if d[i] > 1:
                n = d[i]
                c+=n*(n-1)//2
        return c
        