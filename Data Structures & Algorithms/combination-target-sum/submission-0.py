class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        length = len(nums)

        def dfs(i, cur_list, total):
            if total == target:
                res.append(cur_list.copy())
                return
            
            for j in range(i, length):
                if nums[j] + total > target:
                    return

                cur_list.append(nums[j])
                dfs(j, cur_list, total + nums[j])
                cur_list.pop()


        
        dfs(0, [], 0)
        return res