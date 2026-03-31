class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        i = 0

        while i < n - 2 and nums[i] <= 0:

            # ① i 去重
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            target = -nums[i]
            j = i + 1
            k = n - 1   # ② 每輪 i 重設 k

            while j < k:
                two_sum = nums[j] + nums[k]

                if two_sum > target:
                    k -= 1
                elif two_sum < target:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])

                    # ③ j 去重
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1

                    # ④ k 去重
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    j += 1
                    k -= 1

            i += 1

        return res
