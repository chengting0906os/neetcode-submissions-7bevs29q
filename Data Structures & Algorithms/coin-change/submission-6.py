class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        q = deque([(amount, 0)])   # (remaining_amount, steps)
        visited = set([amount])

        while q:
            rem, step = q.popleft()

            for c in coins:
                nxt = rem-c
                if nxt == 0:
                    return step + 1
                
                if nxt >= 0 and nxt not in visited:
                    visited.add(nxt)
                    q.append([nxt, step+1])



        return -1
