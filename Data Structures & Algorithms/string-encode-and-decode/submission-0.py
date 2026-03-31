class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for char in strs:
            res += str(len(char)) + '#' + char
        return res
        
    def decode(self, s: str) -> List[str]:
        res = []
        n = len(s)
        i = 0

        while i < n:
            for j in range(i, n):
                if s[j] == '#':
                    L = int(s[i:j])      # 長度字段
                    start = j + 1
                    end = start + L
                    res.append(s[start:end])
                    i = end              # 移到下一段的開頭
                    break
        return res


        
        