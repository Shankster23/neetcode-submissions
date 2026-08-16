class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = dict()
        res = []
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in my_dict:
                res.append(my_dict[difference])
                res.append(i)
                return res
            my_dict[nums[i]] = i
        return res