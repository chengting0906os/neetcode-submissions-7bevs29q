class Solution:

    def encode(self, strs: List[str]) -> str:
        # For each item add 字長 + # + 字 in the end
        res = ''
        for s in strs:
            res += str(len(s))
            res += "#"
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        # when i < len(s): keep encoding

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        
        return res
