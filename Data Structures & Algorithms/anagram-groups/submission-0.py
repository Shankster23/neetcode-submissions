class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        my_dict = dict()
        for k in strs:
            sorted_strs.append(''.join(sorted(k)))
        for i in range(len(strs)):
            if sorted_strs[i] in my_dict:
                my_dict[sorted_strs[i]].append(strs[i])
            else:
                my_dict[sorted_strs[i]] = [strs[i]]
        return list(my_dict.values())