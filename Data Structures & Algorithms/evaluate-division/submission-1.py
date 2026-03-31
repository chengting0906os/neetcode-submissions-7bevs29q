class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        res = []
        for i in range(len(equations)):
            x, y = equations[i]
            v = values[i]
            graph[x].append((y, v))
            graph[y].append((x, 1 / v))
        

        def dfs(src, dst, visited):
            if src not in graph or dst not in graph:
                return -1.0
            if src == dst:
                return 1.0

            visited.add(src)
            for nei, value in graph[src]:
                if nei not in visited:
                    result = dfs(nei, dst, visited)
                    if result != -1.0:
                        return result * value
            
            return -1.0



        for x, y in queries:
            res.append(dfs(x, y, set()))
        
        return res


