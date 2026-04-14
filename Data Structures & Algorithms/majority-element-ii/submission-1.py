class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
            
            if len(count) <= 2:
                continue
            
            else:
                new_count = defaultdict(int)
                for k, v in count.items():
                    v -= 1
                    if v != 0:
                        new_count[k] = v
                count = new_count
        
        res = []
        for k in count:
            if nums.count(k) > len(nums) // 3:  
                res.append(k)
        
        return res
