class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        n = len(nums)
        hash_set = {}

        for num in nums:
            hash_set[num] = hash_set.get(num, 0) + num    

        values = sorted(hash_set.keys())
        memo = {}
        def dfs(i):
            if i >= len(values):
                return 0
            if i in memo:
                return memo[i]
            conflicting = (i + 1 < len(values) and values[i + 1] == values[i] + 1)
            take = hash_set[values[i]] + dfs(i + 2) if conflicting else hash_set[values[i]] + dfs(i + 1)
            skip_current =  dfs(i + 1)
            memo[i] = max(skip_current, take)
            return max(skip_current, take)

        return dfs(0)
