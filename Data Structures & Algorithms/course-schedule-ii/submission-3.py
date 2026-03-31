class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        # indegree: how many pre point to c
        # pre: [c, c]
        for c, pre in prerequisites:
            indegree[c] += 1
            adj[pre].append(c)
        
        res = []
        queue = deque()

        for c, num in enumerate(indegree):
            if num == 0:
                queue.append(c)

        while queue:
            c = queue.popleft()
            res.append(c)

            for nxt in adj[c]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    queue.append(nxt)
            
        
        return res if len(res) == numCourses else []