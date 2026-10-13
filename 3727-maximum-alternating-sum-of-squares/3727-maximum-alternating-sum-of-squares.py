class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums2 = []

        for num in nums:
            nums2.append(num**2)

        nums2 = sorted(nums2)

        a = nums2[0:n//2]
        b = nums2[n//2:]

        score = sum(b) - sum(a)

        return score