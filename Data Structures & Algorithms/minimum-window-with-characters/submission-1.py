class Solution:
    def minWindow(self, s: str, t: str) -> str:

        count = defaultdict(int)
        window = defaultdict(int)
        for char in t:
            count[char] += 1
        
        have = 0
        need = len(count)
        l = 0
        res = (float('inf'), float('inf')) # (length, l)

        for r, char in enumerate(s):
            window[char] += 1
            if window[char] == count[char]:
                have += 1
            
            while have == need:
                window[s[l]] -= 1
                if res[0] > r-l+1:
                    res = (r-l+1, l)
                if window[s[l]] < count[s[l]]:
                    have -= 1
                l += 1
                    
        
        return s[res[1]:res[1]+res[0]] if res[0] != float('inf') else ""
        


        


        