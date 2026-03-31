class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_dict = {}
        
        for i, n in enumerate(nums):
            gap = target - n
            if gap in temp_dict:
                return [temp_dict[gap], i]
            else:
                temp_dict[n] = i        