from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
        # dp[i+1], dp[i+2], dp[i+3]를 저장할 변수들
        # 초기값 0: 돌이 더 이상 없으면 점수 차이는 0
        dp_i1 = 0  # dp[i+1]
        dp_i2 = 0  # dp[i+2]
        dp_i3 = 0  # dp[i+3]
        
        # 뒤에서부터 앞으로 순회
        for i in range(n - 1, -1, -1):
            # 1) 현재 돌 1개만 가져가는 경우
            best = stoneValue[i] - dp_i1
            
            # 2) 현재 돌 2개를 가져가는 경우 (i+1이 존재해야 함)
            if i + 1 < n:
                best = max(best, stoneValue[i] + stoneValue[i+1] - dp_i2)
            
            # 3) 현재 돌 3개를 가져가는 경우 (i+2가 존재해야 함)
            if i + 2 < n:
                best = max(best, stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp_i3)
            
            # 현재 상태 dp[i]를 구했으니, 다음 루프(i-1)를 위해 변수들을 한 칸씩 밀어줌
            # dp[i+3] <- dp[i+2], dp[i+2] <- dp[i+1], dp[i+1] <- dp[i]
            dp_i3, dp_i2, dp_i1 = dp_i2, dp_i1, best
        
        # dp[0]이 최종 점수 차이 (Alice - Bob)
        if dp_i1 > 0:
            return "Alice"
        elif dp_i1 < 0:
            return "Bob"
        else:
            return "Tie"