class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        length = len(candidates)
        candidates.sort()

        def dfs(i, cur_list, total):
            if total == target:
                res.append(cur_list.copy())
                return 

            for j in range(i, length):
                if j > i and candidates[j-1] == candidates[j]:
                    continue
                if candidates[j] + total > target:
                    return 
                
                cur_list.append(candidates[j])
                dfs(j+1, cur_list, candidates[j] + total)
                cur_list.pop()

        
        dfs(0, [], 0)
        return res