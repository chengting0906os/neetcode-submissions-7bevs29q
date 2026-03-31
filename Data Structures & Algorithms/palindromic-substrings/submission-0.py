class Solution:
    def countSubstrings(self, s: str) -> int:
        manacher_s = "^#" + "#".join(s) + "#$"
        n = len(manacher_s)
        center, right = 0, 0 
        ps = [0] * n

        for i in range(1, n-1):
            if i < right:
                ps[i] = min(ps[center- (i - center)], right-i)


            while manacher_s[i - ps[i] - 1] == manacher_s[i + ps[i] + 1]:
                ps[i] += 1

            if i + ps[i] > right:
                center = i
                right = i + ps[i]
        

        return sum((v + 1)//2 for v in ps)