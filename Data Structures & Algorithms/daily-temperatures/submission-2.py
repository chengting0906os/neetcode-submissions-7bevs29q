class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        # 每次 append index 到 stack
        # 如果現在的溫度大於最後一個索引位置的值 pop 並相減

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                pre_idx = stack.pop()
                res[pre_idx] = i-pre_idx
            stack.append(i)

        return res