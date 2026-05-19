class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        b = set(nums2)
        for a in nums1:
            if a in b:
                return a
        return -1