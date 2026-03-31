class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        l = 0
        r = l + k
        visited = set()
        
        for i in range(len(nums)):
            if i >= k + 1:
                visited.discard(nums[i-k-1])
            if nums[i] in visited:
                return True
            visited.add(nums[i])

        return False