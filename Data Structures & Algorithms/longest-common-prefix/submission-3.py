class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        i = 0

        while True:
            for s in strs:
                if i >= len(s) or s[i] != strs[0][i]:
                    return ans
            ans += strs[0][i]
            i += 1
