class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_product = nums[0]
        max_product = nums[0]
        res = nums[0]

        for n in nums[1:]:
            tmp = max_product * n
            max_product = max(tmp, min_product *n, n)
            min_product = min(tmp, min_product *n, n)
            res = max(res, max_product)

        return res