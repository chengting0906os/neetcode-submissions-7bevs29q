class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result_dict = {}
        for char in s:
            if result_dict.get(char):
                result_dict[char] += 1 
            else:
                result_dict[char] = 1

        for char in t:
            if result_dict.get(char, None) is None:
                return False
            else:
                result_dict[char] -= 1
        
        for k, v in result_dict.items():
            if v != 0:
                return False

        
        return True