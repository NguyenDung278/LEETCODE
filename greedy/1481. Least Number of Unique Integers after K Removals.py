from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr, k: int) -> int:
        counts = Counter(arr)
        ordered = sorted(counts.values(), reverse=True)

        while k:
            val = ordered[-1]
            if val <= k:
                k -= val
                ordered.pop()
            else:
                break

        return len(ordered)
c = Solution()
arr = [4,3,1,1,3,3,2]
k = 3
print(c.findLeastNumOfUniqueInts(arr,k))