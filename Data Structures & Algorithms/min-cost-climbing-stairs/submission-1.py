class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mem = [None] * (len(cost) + 1)

        def dfs(i):
            if i > (len(cost) - 1):
                return 0

            elif mem[i] != None:
                return mem[i]

            else:
                mem[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
                return mem[i]


        return min(dfs(0), dfs(1))
