class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        max_p = max(people)
        count = [0] * (max_p + 1)
        for p in people:
            count[p] += 1

        i = 0
        j = 1
        while i < len(people):
            while count[j] == 0:
                j += 1          
            people[i] = j
            count[j] -= 1
            i += 1

        res = 0
        l = 0
        r = len(people) - 1    
        while l <= r:
            remain = limit - people[r]
            r -= 1
            res += 1
            if l <= r and remain >= people[l]:  
                l += 1
        return res