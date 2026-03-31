class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack=[]

        cars = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        stack.append((target-cars[0][0])/cars[0][1])


        for pos, s in cars[1:]:
            time = (target-pos) / s
            if stack and time > stack[-1]:
                stack.append(time)

        
        return len(stack)