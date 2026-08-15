class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        xor_sum = 0
        zero_count = 0


        for x in nums:
            xor_sum ^= x
            if x == 0:
                zero_count += 1
        
        if xor_sum != 0:
            return n
        elif zero_count == n:
            return 0
        else:
            return n-1