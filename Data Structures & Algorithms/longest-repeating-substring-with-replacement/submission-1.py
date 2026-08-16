class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_dict = dict()
        max_freq = 0
        left = 0
        max_window_size = 0
        for right in range(len(s)):
            if s[right] in my_dict:
                my_dict[s[right]]+=1
                max_freq = max(my_dict.values())
            if s[right] not in my_dict:
                my_dict[s[right]] = 1
                max_freq = max(my_dict.values())
            while (right - left+1) - max_freq > k:
                if s[left] in my_dict:
                    my_dict[s[left]]-=1
                    if my_dict[s[left]] == 0:
                        del my_dict[s[left]]
                left+=1
                if len(my_dict) !=0:
                    max_freq = max(my_dict.values())
            current_size = right - left + 1
            max_window_size = max(max_window_size, current_size)
        return max_window_size