class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # record the biggest index of this char
        mp = {}
        res = []
        farthest = 0
        first = 0
        for i, char in enumerate(s):
            mp[char] = i
        

        # change your max steps until you reach it and append it to res

        for i, char in enumerate(s):
            farthest = max(mp[char], farthest)
            
            if i == farthest:
                res.append(farthest-first+1)
                first = i + 1
        
        return res