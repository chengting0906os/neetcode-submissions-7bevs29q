class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_freq = max(count.values())
        max_count = sum(1 for c in count.values() if c == max_freq)
        
        # 公式：(max_freq - 1) * (n + 1) + max_count
        min_intervals = (max_freq - 1) * (n + 1) + max_count
        
        # 但不能少於任務總數
        return max(min_intervals, len(tasks))
