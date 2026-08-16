class Solution:
    def findMin(self, nums: List[int]) -> int:
        lo = 0
        hi = len(nums) - 1
        mid = lo+ (hi-lo)//2
        while (nums[mid - 1] <= nums[mid]):
            mid = lo+ (hi-lo)//2
            if len(nums) == 1:
                    return nums[hi]
            if mid == 0:
                if nums[mid] < nums[mid+1]:
                    return nums[mid]
                else:
                    return nums[mid+1]
            elif nums[hi] > nums[mid]:
                hi = mid - 1
            elif nums[hi] < nums[mid]:
                lo = mid+1
            elif nums[hi] == nums[mid]:
                hi = mid - 1
        return nums[mid]