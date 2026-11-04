class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)

        mem = [-1] * (l + 1)

        def dhs(i):
            if i >= l:
                return 0

            elif mem[i] != -1:
                return mem[i]

            else:
                mem[i] = cost[i] + min(dhs(i + 1), dhs(i + 2))
                return mem[i]

        return min(dhs(0), dhs(1))