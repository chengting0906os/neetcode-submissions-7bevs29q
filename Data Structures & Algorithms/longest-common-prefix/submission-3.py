class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        idx = 0

        for i in range(len(strs[0])):
            for word in strs:
                if i >= len(word) or word[i] != strs[0][i]:
                    return strs[0][:idx]
            idx += 1
        
        return strs[0][:idx]
            
