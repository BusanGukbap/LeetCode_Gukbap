from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        num_set = set(nums)
        
        prefix_sum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                break
        
        missing = prefix_sum
        while missing in num_set:
            missing += 1
            
        return missing