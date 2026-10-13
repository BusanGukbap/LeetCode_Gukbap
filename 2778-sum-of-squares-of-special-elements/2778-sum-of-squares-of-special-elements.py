class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n = len(nums)

        answer = 0

        for i in range(n):
            index = i + 1
            
            if n % index == 0:
                answer += nums[i] ** 2
        
        return answer