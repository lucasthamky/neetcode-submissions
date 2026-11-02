class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        def h():
            temp = nums[0]
            for i in range(1, len(nums)):
                temp2 = nums[i] 
                nums[i] = temp
                temp = temp2

            nums[0] = temp

        for x in range(k):
            h()


