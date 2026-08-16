class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        max_count = 0
        for x in hash_set:
            count = 1
            if(x-1 in hash_set):
                continue
            while(x+1 in hash_set):
                count+=1
                x+=1
            if count > max_count:
                max_count = count
        return max_count