class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)

        def backtrack(cur_list: List[int], pick: List[bool]):
            if len(cur_list) == length:
                res.append(cur_list.copy())
                return 
            for i in range(length):
                if pick[i] is False:
                    cur_list.append(nums[i])
                    pick[i] = True
                    backtrack(cur_list, pick)
                    cur_list.pop()
                    pick[i] = False

        

        backtrack([], [False]*length)
        return res
