class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for i in range(len(strs)):
            sortedStr = tuple(sorted(strs[i]))
            hashmap[sortedStr].append(strs[i])

        return list(hashmap.values())