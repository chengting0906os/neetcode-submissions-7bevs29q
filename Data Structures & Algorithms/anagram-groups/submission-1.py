class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 創建一個 dict 丟進去
        # traverse 
        mp = defaultdict(list)
        res = []

        for s in strs:
            sorted_s = "".join(sorted(s))
            mp[sorted_s].append(s)
        
        for v in mp.values():
            res.append(v)
        
        return res