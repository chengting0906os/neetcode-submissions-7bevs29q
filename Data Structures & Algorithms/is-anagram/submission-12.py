class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = Counter(s)

        for char in t:
            mp[char] = mp.get(char, 0) - 1
        
        for count in mp.values():
            if count != 0:
                return False
        
        return True