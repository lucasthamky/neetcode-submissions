class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(left, right):
            i = j = 0
            res = []

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res.append(left[i])
                    i += 1

                else:
                    res.append(right[j])
                    j += 1

            res.extend(left[i:])
            res.extend(right[j:])
            return res
                
        if len(nums) <= 1:
            return nums

        length = len(nums)
        mid = len(nums)//2

        left = nums[:mid]
        right = nums[mid:]
        sortedLeft = self.sortArray(left)
        sortedRight = self.sortArray(right)

        return merge(sortedLeft, sortedRight)