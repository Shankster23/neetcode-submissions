class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0]*len(nums)
        prefix_products = [0] * len(nums)
        suffix_products = [0] * len(nums)
        prefix_products[0] = 1
        suffix_products[len(nums) -1] = 1
        for i in range(1, len(nums)):
            prefix_products[i] = prefix_products[i - 1]*nums[i-1]
        for i in range(len(nums) - 2, -1,-1):
            suffix_products[i] = suffix_products[i + 1]* nums[i+1] 
        for i in range(len(nums)):
            answer[i] = prefix_products[i]*suffix_products[i]
        return answer