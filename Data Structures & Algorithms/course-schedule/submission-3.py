class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        for c, pre in prerequisites:
            adj[pre].append(c)
            indegree[c] += 1

        queue = deque()
        for c, num in enumerate(indegree): 
            if num == 0:
                queue.append(c)
                
        finish = 0
        while queue:
            finish += 1
            c = queue.popleft()
            for nei in adj[c]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    queue.append(nei)




        return finish == numCourses