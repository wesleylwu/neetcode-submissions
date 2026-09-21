class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        res = []
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for n, i in count.items():
            freq[i].append(n)

        for i in range(len(freq) - 1, 0, -1):
            for j in freq[i]:
                res.append(j)
                if k == len(res):
                    return res
        return