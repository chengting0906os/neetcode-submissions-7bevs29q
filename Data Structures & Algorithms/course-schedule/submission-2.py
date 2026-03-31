class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        mp = {i:[] for i in range(numCourses)}

        for c, pre in prerequisites:
            mp[c].append(pre)

        visited = set()

        def dfs(c):
            if c in visited:
                return False

            if mp[c] == []:
                return True
            
            visited.add(c)
            for pre in mp[c]:
                if not dfs(pre):
                    return False
            visited.remove(c)
            mp[c] = []
            
            return True
            

        
        for c in mp.keys():
            if not dfs(c):
                return False

        return True



