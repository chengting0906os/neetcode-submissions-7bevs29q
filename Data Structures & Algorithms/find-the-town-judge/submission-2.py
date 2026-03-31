class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        mp = defaultdict(int)

        for src, dst in trust:
            mp[src] -= 1
            mp[dst] += 1

        for i in range(1, n + 1):
            if mp[i] == n - 1:
                return i

        return -1
