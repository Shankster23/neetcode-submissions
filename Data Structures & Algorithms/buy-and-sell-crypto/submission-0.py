class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        global_max = 0
        left = 0
        for right in range(len(prices)):
            local_max = prices[right] - prices[left]
            while prices[left] > prices[right]:
                left+=1
            if local_max > global_max:
                global_max = local_max
        return global_max