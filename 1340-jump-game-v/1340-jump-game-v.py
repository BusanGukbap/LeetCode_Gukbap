class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        N = len(arr)
        dp = dict()
        
        def dfs(pos):
            if pos in dp:
                return

            dp[pos] = 1
            
            # 왼쪽으로 점프하기
            next_pos = pos - 1
            while next_pos >= 0 and pos - next_pos <= d and arr[pos] > arr[next_pos]:
                dfs(next_pos)
                dp[pos] = max(dp[pos], dp[next_pos] + 1)
                next_pos -= 1
            
            # 오른쪽으로 점프하기
            next_pos = pos + 1
            while next_pos < N and next_pos - pos <= d and arr[pos] > arr[next_pos]:
                dfs(next_pos)
                dp[pos] = max(dp[pos], dp[next_pos] + 1)
                next_pos += 1

        for i in range(N):
            dfs(i)


        return max(dp.values())
