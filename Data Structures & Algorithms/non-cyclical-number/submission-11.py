class Solution:
    def isHappy(self, n: int) -> bool:
        bucket = set()
        bucket.add(n)
        while True:
            num = self.mul(n)
            if num == 1:
                return True
            if num in bucket:
                return False
            bucket.add(num)
            n = num
    


    def mul(self, n):
        res = 0
        while n:
            rem = n % 10
            res += rem * rem
            n = n // 10

        return res