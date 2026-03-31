class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x, y in points[:k]:
            dist = x*x + y*y
            heap.append((-dist, [x, y]))  

        heapq.heapify(heap)

        for x, y in points[k:len(points)]:
            dist = x*x + y*y
            heapq.heappushpop(heap, (-dist, [x, y]))
        

        return [ans for dist, ans in heap]