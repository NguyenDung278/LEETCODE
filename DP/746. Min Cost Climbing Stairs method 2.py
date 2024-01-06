class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        mini_cost = [0]* (len(cost)+1)
        for i in range(2,len(cost)+1):
            one_step = mini_cost[i-1]+ cost[i-1]
            two_step = mini_cost[i-2]+ cost[i-2]
            mini_cost[i] = min(one_step,two_step)
        return mini_cost[-1]