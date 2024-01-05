from collections import Counter
class Solution:
    def findLucky(self, arr) -> int:
        s = Counter(arr)
        result = -1
        for c in arr:
            if s[c]==c:
                result = max(result,c)
        return result
arr = [2,2,3,4]
s = Solution()
print(s.findLucky(arr))