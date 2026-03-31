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
        res = [""]

        for digit in digits:
            tmp = []
            for cur_str in res:
                for char in mp[digit]:
                    tmp.append(cur_str+char)
            res = tmp
        return res

        