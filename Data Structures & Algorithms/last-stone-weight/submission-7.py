class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) >= 2 :
            a = heapq.heappop(stones) * -1
            b = heapq.heappop(stones) * -1 
            if a - b > 0:
                heapq.heappush(stones, -(a - b))
        
        return -stones[0] if stones else 0