class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = Counter(nums)
        bucket = [[] for _ in range(len(nums)+1)]
        res = []

        for n, count in mp.items():
            bucket[count].append(n)
        
        for i in range(len(bucket)-1, -1, -1):
            if bucket[i]:
                for n in bucket[i]:
                    res.append(n)
                    if len(res) == k:
                        return res
         