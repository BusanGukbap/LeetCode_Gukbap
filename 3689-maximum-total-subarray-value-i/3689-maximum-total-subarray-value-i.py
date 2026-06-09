class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        n = len(nums)

        value = max(nums) - min(nums)

        return k * value