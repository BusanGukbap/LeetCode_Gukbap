class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        nums.append(nums[0])
        
        cnt = 0

        for i in range(n):
            if nums[i+1] - nums[i] < 0:
                cnt += 1
        
        if cnt > 1:
            return False
        return True