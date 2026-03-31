class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        pre_time = 0
        res = 0

        for position, speed in cars:
            now_time = (target - position) / speed
            if now_time > pre_time:
                res += 1
                pre_time = now_time
        
        return res
