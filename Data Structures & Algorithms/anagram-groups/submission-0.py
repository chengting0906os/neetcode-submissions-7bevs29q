class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for char in strs:
            bucket = [0] * 26
            for c in char:
                bucket[ord(c) - ord('a')] += 1

            res[tuple(bucket)].append(char)

        return list(res.values())