class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)

        F = []
        cur = 0
        for i in range(n):
            cur += i * nums[i]
        
        F.append(cur)

        total = sum(nums)
        for i in range(1, n):
            temp = F[i-1] + total
            temp -= nums[n-i]*(n)
            F.append(temp)
        
        return max(F)