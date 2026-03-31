class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res = 0

        while l <= r:
            mid = (r-l)//2 + l
            num_of_time = 0

            for p in piles:
                num_of_time += math.ceil((p / mid))
            
            if num_of_time > h:
                l = mid + 1 
            else:
                res = mid
                r = mid - 1
        
        return res