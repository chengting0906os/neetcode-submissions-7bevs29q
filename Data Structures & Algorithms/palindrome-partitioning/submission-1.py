class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []
        
        def dfs(i):
            if i == len(s):
                res.append(part.copy())
                return
            
            for j in range(i, len(s)):
                if self.is_pali(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res
    
    def is_pali(self, string):
        l = 0 
        r = len(string) - 1
        while l < r:
            if string[l] == string[r]:
                l += 1
                r -= 1
            else:
                return False
        return True