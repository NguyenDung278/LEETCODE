class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(i): 
            if i <= 2: 
                return i
            if i not in meno:
                meno[i] = dp(i-1)+dp(i-2)
        
            return meno[i]
        meno = {}
        return dp(n)

