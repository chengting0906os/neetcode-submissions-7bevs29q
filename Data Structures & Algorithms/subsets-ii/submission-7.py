class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        temp = []

        def dfs(start):
            res.append(temp.copy())

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue
                temp.append(nums[i])
                dfs(i+1)
                temp.pop()

        
        dfs(0)
        return res