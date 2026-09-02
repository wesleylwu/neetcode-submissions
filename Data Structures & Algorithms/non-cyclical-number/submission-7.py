class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            arr = [int(s) for s in str(n)]
            n = sum([num**2 for num in arr])
            if n == 1:
                return True
        return False