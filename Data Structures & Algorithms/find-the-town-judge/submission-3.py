class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # 有主動信任別人的人 → 不可能是法官
        trusts_someone = {a for a, b in trust}
        
        # 被所有人信任的人 → 法官候選
        trusted_by = Counter(b for a, b in trust)

        for i in range(1, n + 1):
            if i not in trusts_someone and trusted_by[i] == n - 1:
                return i
        
        return -1