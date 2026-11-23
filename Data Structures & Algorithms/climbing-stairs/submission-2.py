class Solution:
    def climbStairs(self, n: int) -> int:
        mem = [None] * (n + 1)

        def dfs(step):
            if step > n:
                return 0
            elif step == n:
                return 1

            elif mem[step] != None:
                return mem[step]
            
            else:
                mem[step] = dfs(step + 1) + dfs(step + 2)
                return mem[step]
        
        return dfs(0)