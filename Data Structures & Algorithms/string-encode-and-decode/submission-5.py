class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ''

        for s in strs:
            code += str(len(s)) + '#' + s
        
        return code

    def decode(self, s: str) -> List[str]:
        code, i = [], 0

        while i < len(s):
            j = i

            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            code.append(s[j + 1:length + j + 1])
            i = length + j + 1
        return code