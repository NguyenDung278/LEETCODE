class Solution(object):
    def numJewelsInStones(self, J, S):
        Jset = set(J)
        return sum(s in Jset for s in S)
    
jewels = "aA" 
stones = "aAAbbbb"
S = Solution()
print(S.numJewelsInStones(jewels,stones))