class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        for loop 
        
        """

        count = Counter(nums)
        res = []

        for k, v in count.items():
            if v > len(nums) // 3:
                res.append(k)

        return res