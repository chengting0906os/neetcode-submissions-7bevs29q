class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        mp = defaultdict(int)
        for i, n in enumerate(numbers):
            gap = target - n
            if gap in mp:
                return [mp[gap]+1, i+1]
            else:
                mp[n] = i
                
