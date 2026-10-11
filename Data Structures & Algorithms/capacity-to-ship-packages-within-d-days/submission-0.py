class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        n = len(weights)
        def possible(capacity):
            count = 1
            num = 0
            for i in range(n):
                if num + weights[i] > capacity:
                    count+= 1
                    num = 0
                num+=weights[i]
            return count
        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = lo + (hi - lo) //2
            if possible(mid) <= days:
                hi = mid
            else:
                lo = mid + 1
        return lo


