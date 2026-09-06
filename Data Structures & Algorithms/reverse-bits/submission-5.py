class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            res = res << 1
            bit = n % 2
            n = n >> 1
            res += bit
        return res