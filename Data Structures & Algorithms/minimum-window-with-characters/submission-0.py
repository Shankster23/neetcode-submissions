class Solution:
    def is_valid(self, t_freq_dict: dict, window_freq_dict: dict) -> bool:
        #iterate through and if window_freq_dict is less then return false
        for char in t_freq_dict:
            if window_freq_dict.get(char, 0) < t_freq_dict[char]:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        t_freq_dict = dict()
        window_freq_dict = dict()
        res = ""
        #populate t with its frequencies
        for k in t:
            t_freq_dict[k] = t_freq_dict.get(k, 0) + 1
        #sliding window
        for right in range(len(s)):
            window_freq_dict[s[right]] = window_freq_dict.get(s[right], 0) + 1
            left_char = s[left]
            while left < len(s) and (window_freq_dict.get(left_char, 0) > t_freq_dict.get(left_char, 0) or left_char not in t_freq_dict) and self.is_valid(t_freq_dict, window_freq_dict):
                window_freq_dict[left_char]-=1
                left+=1
                if left < len(s):  # Add this bounds check
                    left_char = s[left]
            if(self.is_valid(t_freq_dict, window_freq_dict) and (len(s[left:right+1]) < len(res) or res == "")):
                res = s[left:right+1]
        return res