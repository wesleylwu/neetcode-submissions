class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            arr = [int(s) for s in str(n)]
            n = sum([v**2 for v in arr])
            if n == 1:
                return True
        return False