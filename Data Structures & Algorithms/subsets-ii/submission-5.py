class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        left_bound = 0
        right_bound = 0
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                left_bound = right_bound
            else:
                left_bound = 0

            right_bound = len(res)
            for j in range(left_bound, right_bound):
                temp = res[j].copy()
                temp.append(nums[i])
                res.append(temp)
                

        return res