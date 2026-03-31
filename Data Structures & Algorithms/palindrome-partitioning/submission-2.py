from functools import lru_cache

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)

        @lru_cache(None)
        def isPali(i, j):
            if i >= j:
                return True
            if s[i] != s[j]:
                return False
            return isPali(i + 1, j - 1)

        def dfs(i):
            if i == n:
                return [[]]

            res = []
            for j in range(i, n):
                if isPali(i, j):
                    for rest in dfs(j + 1):
                        res.append([s[i:j+1]] + rest)
            return res

        return dfs(0)