class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def days_needed(capacity):
            days_used = 1
            current_load = 0
            for weight in weights:
                if current_load + weight > capacity:
                    days_used += 1
                    current_load = 0
                current_load += weight
            return days_used

        lo, hi = max(weights), sum(weights)
        while lo < hi:
            mid = (lo + hi) // 2
            if days_needed(mid) <= days:
                hi = mid
            else:
                lo = mid + 1
        return lo