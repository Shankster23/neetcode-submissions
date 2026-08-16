class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_dict = dict()
        for i in range(len(nums)):
            if(nums[i] not in freq_dict):
                freq_dict[nums[i]] = 1
            else:
                freq_dict[nums[i]]+=1
        res = heapq.nlargest(k, freq_dict.keys(), lambda num: freq_dict[num])
        return res