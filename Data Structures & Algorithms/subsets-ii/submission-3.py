from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]

        prev_size = 0  # 記錄上一輪 res 的大小

        for i in range(len(nums)):
            # 如果是重複數字，只從上一輪新增的 subset 開始擴展
            if i > 0 and nums[i] == nums[i - 1]:
                start = prev_size
            else:
                start = 0

            prev_size = len(res)

            for j in range(start, prev_size):
                res.append(res[j] + [nums[i]])

        return res