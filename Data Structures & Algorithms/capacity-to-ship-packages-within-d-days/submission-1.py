class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasibility(x):
            total = 0
            D = 1
            for i in weights:
                total = total + i
                if total > x:
                    D += 1
                    total = i

            if D > days:
                return False
            
            return True

        l, r = max(weights), sum(weights)

        while l <= r:
            mid = (l + r)//2

            if feasibility(mid):
                r = mid - 1

            else:
                l = mid + 1

        return l


