class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        mem = [None] * (l + 1)

        def dfs(i):
            if i >= l:
                return 0

            elif mem[i] != None:
                return mem[i]
            
            else:
                mem[i] = nums[i] + max(dfs(i + 2), dfs(i + 3))
                return mem[i]

        return max(dfs(0), dfs(1))

        