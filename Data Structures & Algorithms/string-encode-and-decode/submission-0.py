class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for k in strs:
            res+=str(len(k))
            res+=":"
            res+=k
        return res
        

    def decode(self, s: str) -> List[str]:
        res = []
        while(len(s) != 0):
            index = s.find(":")
            length_count = int(s[0:index])
            word = s[index+1:index+length_count+1]
            res.append(word)
            s = s[index+length_count+1:]
        return res


