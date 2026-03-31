class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_l = 0 
        mp = defaultdict(int) # 紀錄現在在區間裡的當前 key 的長度
        l = 0
        res = 0

        # 每次向右移動 計算 r - l + 1 - max_l >= k 
        for r, char in enumerate(s):
            mp[char] += 1
            max_l = max(max_l, mp[char])
            if r - l + 1 - max_l > k:
                mp[s[l]] -= 1
                l += 1
            res = max(res, r-l+1)

            
            
        
        return res

