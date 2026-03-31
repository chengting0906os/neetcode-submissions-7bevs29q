class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        """
        a_b     insert

        aab 

        aab     delete 
         x  
        ab 

        aaccc   delete remaing

        aa

        aa___   insert remaing
        aaccc
        """
        if len(word2) > len(word1):
            word1, word2 = word2, word1
        
        n = len(word1)
        m = len(word2)
        dp = {}
        def dfs(i, j):
            if i == len(word1):
                return m - j
            if j == len(word2):
                return n - i
            
            if word1[i] == word2[j]:
                dp[(i,j)] = dfs(i+1, j+1)
            else:
                res = min(dfs(i+1, j), dfs(i, j+1), dfs(i+1, j+1)) 
                dp[(i,j)] = res + 1
            return dp[(i, j)]

        
        return dfs(0,0)
