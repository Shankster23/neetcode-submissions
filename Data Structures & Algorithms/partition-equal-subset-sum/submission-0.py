class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        memo = {}
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        def dfs(i, remaining):
            if remaining < 0:
                return False
            if remaining == 0:
                return True
            if i == len(nums):
                return False
            if (i, remaining) in memo:
                return memo[(i, remaining)]
            
            take = dfs(i + 1, remaining - nums[i])
            if take:
                memo[(i, remaining)] = True
                return True
            skip = dfs(i + 1, remaining)
            memo[(i, remaining)] =skip
            return skip
            
        return dfs(0, target)
        
            

        