class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        res = []
        for i in range(len(nums)):
            if nums[i] == nums[i - 1] and i != 0:
                continue
            target = 0 - nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                sum = nums[left] + nums[right]
                if sum == target:
                    res.append([nums[i], nums[left], nums[right]])
                    left+=1
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    right-=1
                    while left < right and right < len(nums) - 1 and nums[right] == nums[right+1]:
                        right-=1
                if sum < target:
                    left+=1
                if sum > target:
                    right-=1
        return res