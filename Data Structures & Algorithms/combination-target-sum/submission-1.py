class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        if not nums:
            return []
        res = []
        def dfs(idx, amount, curr):
            if idx == len(nums) or amount > target:
                return 

            if amount == target:
                res.append(curr.copy())
                return 

            amount += nums[idx]
            curr.append(nums[idx])
            dfs(idx, amount, curr)

            amount -= nums[idx]
            curr.pop()
            dfs(idx+1, amount, curr)
        
        dfs(idx=0, amount=0, curr=[])
        
        return res
