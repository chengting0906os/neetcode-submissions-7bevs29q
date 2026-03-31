class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1

        max_l = height[l]
        max_r = height[r]
        acc = 0

        while l < r:
            if height[l] < height[r]:
                acc += min(max_l, max_r) - height[l]
                l+= 1
                max_l = max(max_l, height[l])
            else:
                acc += min(max_l, max_r) - height[r]
                r -= 1
                max_r = max(max_r, height[r])
        return acc
                
                 
            


                
                

                
                
                
