class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        new_arr = [None] * (n * 2)
        g = 0

        for i in range(len(new_arr)):
            if g >= n:
                g = g - n
            new_arr[i] = nums[g]
            g = g + 1

        
             

        return new_arr