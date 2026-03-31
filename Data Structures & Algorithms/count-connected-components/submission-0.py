class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        count = 0
        queue = deque()

        for i in range(n):
            if i not in visited:
                queue.append(i)
            
                while queue:
                    node = queue.popleft()
                    visited.add(node)

                    for nei in adj[node]:
                        if nei not in visited:
                            queue.append(nei)
                count += 1

        return count
            