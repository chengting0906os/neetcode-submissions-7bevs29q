class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp_dict = {}
        
        for i in range(len(nums)):
            gap = target - nums[i]
            if gap in temp_dict:
                return [temp_dict[gap], i]
            else:
                temp_dict[nums[i]] = i        