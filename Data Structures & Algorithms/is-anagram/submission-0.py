class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = dict()
        t_set = dict()
        for k in s:
            if k not in s_set:
                s_set[k] = 1
            else:
                s_set[k]+=1
        for g in t:
            if g not in t_set:
                t_set[g] = 1
            else:
                t_set[g]+=1
        return s_set == t_set
        