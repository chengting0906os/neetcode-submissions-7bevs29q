class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        plus = 1
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                if plus:
                    digits[i] = 0
                    plus = 1
            else:
                digits[i] += plus
                plus = 0
        
        if plus:
            digits.insert(0,1)

        return digits

