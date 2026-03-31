class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        need = [0] * 26
        window = [0] * 26
        l = 0

        for char in s1:
            need[ord(char) - ord('a')] += 1
        
        for r, char in enumerate(s2):
            window[ord(char) - ord('a')] += 1
            if r-l == len(s1):
                window[ord(s2[l]) - ord('a')] -= 1
                l += 1
            
            if need == window:
                return True
        
        return False