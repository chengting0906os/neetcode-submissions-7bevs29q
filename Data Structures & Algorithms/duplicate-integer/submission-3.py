class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n_set = set()
        for n in nums:  
            if n in n_set:          
                return True
            else:
                n_set.add(n)
        return False