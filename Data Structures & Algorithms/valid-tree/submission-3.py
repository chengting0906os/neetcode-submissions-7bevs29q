class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adj = [[] for _ in range(n)]

        for parent, child in edges:
            adj[parent].append(child)
            adj[child].append(parent)

        visited = set()

        def bfs(par, child):
            if child in visited:
                return False
            visited.add(child)
            for nei in adj[child]:
                if nei == par:
                    continue
                if not bfs(child, nei):
                    return False

            return True

        return bfs(-1, 0) and len(visited) == n