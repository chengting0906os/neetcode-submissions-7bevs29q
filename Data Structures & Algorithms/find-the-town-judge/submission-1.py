class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        mp = defaultdict(list)
        max_edge = 0
        candidate = 0
        res = False
    
        for a, person in trust:
            mp[person].append(a)
        
        for k, people in mp.items():
            if len(people) >= max_edge:
                max_edge = len(people)
                candidate = k
        
        if max_edge == n - 1:
            res = True
            for person in mp[candidate]:
                if candidate in mp[person]:
                    res = False
        
        if not res:
            return -1
        else:
            return candidate
