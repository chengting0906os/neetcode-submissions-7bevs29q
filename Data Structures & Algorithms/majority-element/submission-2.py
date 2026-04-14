class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        now = 0
        count = 0

        for n in nums:
            if count == 0:
                now = n
            if n == now:
                count += 1
            else:
                count -= 1
        return now
            