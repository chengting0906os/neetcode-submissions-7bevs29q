class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        l = 0
        idx = 0
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                l = idx
            else:
                l = 0

            idx = len(res)
            for j in range(l, idx):
                temp = res[j].copy()
                temp.append(nums[i])
                res.append(temp)
                

        return res