class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        ans = []

        for i in range(0, len(nums)):
            for j in range (i + 1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    if i < j:
                        ans.append(i)
                        ans.append(j)
                        return ans
                    ans.append(j)
                    ans.append(i)
                    return ans
        return ans