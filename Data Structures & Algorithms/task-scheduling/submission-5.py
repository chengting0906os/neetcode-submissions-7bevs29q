import heapq
from collections import Counter, deque
from typing import List

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        # 直接建立 max heap
        max_heap = list(count.values())
        heapq.heapify_max(max_heap)

        time = 0
        cooldown = deque()  # (remaining_count, ready_time)

        while max_heap or cooldown:
            time += 1

            if max_heap:
                cnt = heapq.heappop_max(max_heap) - 1
                if cnt > 0:
                    cooldown.append((cnt, time + n))
            else:
                # idle → jump to next available time
                time = cooldown[0][1]

            if cooldown and cooldown[0][1] == time:
                heapq.heappush_max(max_heap, cooldown.popleft()[0])

        return time
