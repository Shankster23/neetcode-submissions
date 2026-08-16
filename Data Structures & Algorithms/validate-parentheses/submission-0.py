class Solution:
    def isValid(self, s: str) -> bool:
        my_dict = {"(":")","[":"]", "{":"}", ")":"(", "]":"[", "}":"{"}
        stack = deque()
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            if s[i] == ")" or s[i] == "]" or s[i] == "}":
                if len(stack) == 0:
                    return False
                open_bracket = stack.pop()
                #if open_bracket corresponds with the closed bracket
                if open_bracket == my_dict[s[i]]:
                    continue
                else:
                    return False
        return len(stack) == 0