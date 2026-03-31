class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        def dfs(parent, child):
            if child in visited:
                return False
            
            visited.add(child)
            
            for node in adj[child]:
                if node == parent:
                    continue
                if not dfs(child, node):
                    return False

            return True
        

        return dfs(-1, 0) and len(visited) == n
