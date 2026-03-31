class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            if carry:
                if digits[i] + carry == 10:
                    carry = 1
                    digits[i] = 0
                elif digits[i] + carry < 10:
                    digits[i] = digits[i] + carry
                    carry = 0
                    break

        
        if carry:
            digits.insert(0, 1)
        
        return digits
                
