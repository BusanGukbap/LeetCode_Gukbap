class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        return min(
            nums[-1] - nums[2],
            nums[-3] - nums[0],
            nums[-2] - nums[1]
        )    