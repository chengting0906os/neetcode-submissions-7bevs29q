class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def dfs(idx, amount, curr):
            if amount == target:
                res.append(curr.copy())
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                if amount + candidates[i] > target:
                    break
                
                curr.append(candidates[i])
                dfs(i+1, amount + candidates[i], curr)
                curr.pop()
            
        dfs(0, 0, [])
        return res