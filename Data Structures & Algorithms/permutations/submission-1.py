class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return nums

        res = []
        count = len(nums)
        used = [False] * count

        def dfs (path:List[int]):
            if len(path) == count:
                res.append(path.copy())
                return 
            
            for j in range(count):
                if used[j] is False:
                    path.append(nums[j])
                    used[j] = True
                    dfs(path)
                    
                    path.pop()
                    used[j] = False

        dfs(path=[])
        
        return res