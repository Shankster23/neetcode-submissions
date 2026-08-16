class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        #check if section is sorted
        while(left <= right):
            mid = left + (right - left)//2
            if(nums[mid] == target):
                return mid
            elif(nums[mid] >= nums[left]):
                #target in the sort
                if  (nums[left] <= target<= nums[mid]):
                    right = mid - 1
                else:
                    left = mid+1
            elif(nums[right] >= nums[mid]):
                if (nums[mid] <= target <= nums[right]):
                    left = mid+1
                else:
                    right = mid - 1
        return -1
