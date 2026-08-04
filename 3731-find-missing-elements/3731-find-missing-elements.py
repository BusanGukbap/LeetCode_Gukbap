class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        ans = list()

        a = min(nums)
        b = max(nums)

        for i in range(a, b+1):
            if i not in nums:
                ans.append(i)
        return ans