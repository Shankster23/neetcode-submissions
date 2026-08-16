class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        characters = set()
        left = 0
        current_max = 0
        for right in range(len(s)):
            while s[right] in characters:
                characters.remove(s[left])
                left+=1
            if s[right] not in characters:
                characters.add(s[right])
                if len(characters) > current_max:
                    current_max = len(characters)
        return current_max