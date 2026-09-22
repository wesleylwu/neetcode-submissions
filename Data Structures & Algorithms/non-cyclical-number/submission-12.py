class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n not in seen:
            seen.add(n)
            arr = [int(i) for i in str(n)]
            n = sum([i**2 for i in arr])
            if n == 1:
                return True
        
        return False
