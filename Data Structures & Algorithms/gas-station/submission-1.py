class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        cur_gas = 0
        res = 0

        for i in range(n):
            cur_gas = cur_gas + gas[i] - cost[i]
            if cur_gas < 0:
                cur_gas = 0
                res = i + 1
        
        if res >= 0:
            return res
            
        return -1

