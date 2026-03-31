class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_someone = {a for a, b in trust}
        trusted_by = Counter(b for a, b in trust)

        for i in range(1, n+1):
            if i not in trust_someone and i in trusted_by:
                if trusted_by[i] == n - 1:
                    return i
        
        return -1