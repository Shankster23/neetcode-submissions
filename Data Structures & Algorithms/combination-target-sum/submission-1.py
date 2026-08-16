class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        path = []
        def backtrack(workingSum, path, i):
            if sum(workingSum) == target:
                path.append(workingSum[:])
                return
            if i >= len(nums):
                return
            while sum(workingSum) + nums[i] <= target:
                workingSum.append(nums[i])
            while True:
                backtrack(workingSum, path, i+1)
                if not workingSum or workingSum[-1] != nums[i]:
                    break
                workingSum.pop()
        backtrack([], path, 0)
        return path