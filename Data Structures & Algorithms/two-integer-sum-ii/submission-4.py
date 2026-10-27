class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first = 0
        
        def bSearch(numbers, value, lo):
            i = lo
            j = len(numbers) - 1

            while i <= j:
                mid = (i + j)//2
                if numbers[mid] == value:
                    return mid

                elif numbers[mid] < value:
                    i = mid + 1

                else:
                    j = mid - 1    
            return -1

        second = bSearch(numbers, target - numbers[first], first + 1)

        while numbers[first] + numbers[second] != target:
            first = first + 1
            second = bSearch(numbers, target - numbers[first], first + 1)

        
        return [first + 1, second + 1]

        

        
                
        