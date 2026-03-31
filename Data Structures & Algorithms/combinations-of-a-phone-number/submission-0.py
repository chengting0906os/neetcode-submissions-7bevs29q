class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        # create a map
        mp = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        n = len(digits)

        def dfs(i, subset):
            if i == n:
                result = "".join(subset)
                res.append(result)
                return
            
            for char in mp[digits[i]]:
                subset.append(char)
                dfs(i+1, subset)
                subset.pop()

        dfs(0, [])

        return res