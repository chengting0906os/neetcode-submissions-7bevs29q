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

        def dfs(i, sub_str):
            if i == n:
                res.append(sub_str)
                return
            
            for char in mp[digits[i]]:
                dfs(i+1, sub_str+char)

        dfs(0, "")

        return res