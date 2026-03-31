class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 如果區間內的後面有比你大的就會被淘汰
        # 把沒機會被選的踢掉
        res = []
        l = 0
        r = 0
        q = deque()

            
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
         
            q.append(r)
            if l > q[0]:
                q.popleft()
            
            r+=1
            if r  >= k:
                res.append(nums[q[0]])
                l += 1
            
                

        
        return res
            
            




