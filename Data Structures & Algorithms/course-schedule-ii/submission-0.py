class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            indegree[a] += 1
            adj[b].append(a)

        q = deque([i for i in range(numCourses) if indegree[i] == 0])

        res = []
        while q:
            i = q.popleft()
            neiborhoods = adj[i]
            res.append(i)
            numCourses -= 1
            if numCourses == 0:
                return res
            for nei in neiborhoods:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
                    
        return []