class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        rows = len(triplets)
        cols = len(triplets[0])
        skip_row = set()
        res = []

        for j in range(cols):
            for i in range(rows):
                if triplets[i][j] > target[j]:
                    skip_row.add(i)

        for j in range(cols):
            max_cur = 0
            for i in range(rows):
                if i not in skip_row:
                    max_cur = max(max_cur, triplets[i][j])
            if max_cur == target[j]:
                res.append(True)
            else:
                res.append(False)
        return all(res)

                    
       
        