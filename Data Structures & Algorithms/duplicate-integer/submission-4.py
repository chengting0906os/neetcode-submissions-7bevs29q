class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bucket = set()
        for n in nums:
            if n in bucket:
                return True
            bucket.add(n)
        
        return False