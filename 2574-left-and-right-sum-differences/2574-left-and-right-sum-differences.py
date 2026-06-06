class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        N = len(nums)
        answer = list()
        leftSum = list()
        rightSum = list()

        leftSum.append(0)
        rightSum.append(total-nums[0])
        answer.append(abs(leftSum[0]-rightSum[0]))
        
        for i in range(1, N):
            leftSum.append(leftSum[i-1] + nums[i-1])
            rightSum.append(rightSum[i-1] - nums[i])
            answer.append(abs(leftSum[i] - rightSum[i]))
        
        return answer
            