class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        def dp(i):
            if i<=1:
                return 0
            if i in memo:
                return memo[i]
            down_one = cost[i-1] + dp(i-1)
            down_two = cost[i-2] + dp(i-2)
            memo[i] = min(down_one,down_two)
            return memo[i]
        
        memo = {}
        return dp(len(cost))
            