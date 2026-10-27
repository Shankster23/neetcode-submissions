import sys
class Solution:
    def maxSumOfThreeSubarrays(self, nums: list[int], k: int) -> list[int]:
        sys.setrecursionlimit(10**5)
        W = []
        cur = sum(nums[:k])
        W.append(cur)
        for i in range(k, len(nums)):
            cur+= nums[i] - nums[i - k]
            W.append(cur)
        memo = {}
        def f(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            # base cases
            if j == 0:
                return 0
            if i >= len(W): return float('-inf')
            skip = f(i + 1, j)
            take = W[i] + f(i + k, j - 1)
            result = max(skip, take)
            memo[(i, j)] = result
            return result
        f(0, 3)
        res = []
        i, j = 0, 3
        while j > 0:
            take = W[i] + f(i + k, j - 1)
            skip = f(i + 1, j)
            if take >= skip:
                res.append(i)
                i, j = i + k, j - 1
            else:
                i+=1
        return res