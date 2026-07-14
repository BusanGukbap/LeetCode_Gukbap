from typing import List
from math import gcd

class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        MAX_VAL = 200  # 문제 제약 조건 (nums[i] <= 200)

        # dp[g1][g2]: 현재까지 선택한 seq1의 GCD = g1, seq2의 GCD = g2 인 경우의 수
        dp = [[0] * (MAX_VAL + 1) for _ in range(MAX_VAL + 1)]
        dp[0][0] = 1  # 아무것도 선택하지 않은 초기 상태

        for x in nums:
            # 새로운 상태를 저장할 테이블 (0으로 초기화)
            new_dp = [[0] * (MAX_VAL + 1) for _ in range(MAX_VAL + 1)]

            for g1 in range(MAX_VAL + 1):
                for g2 in range(MAX_VAL + 1):
                    cur = dp[g1][g2]
                    if cur == 0:
                        continue

                    # 1. 현재 숫자를 어떤 부분 수열에도 넣지 않음 (Skip)
                    new_dp[g1][g2] = (new_dp[g1][g2] + cur) % MOD

                    # 2. 현재 숫자를 seq1에 추가
                    # gcd(0, x)는 항상 x가 되므로, 분기 처리가 따로 필요 없음
                    ng1 = gcd(g1, x)
                    new_dp[ng1][g2] = (new_dp[ng1][g2] + cur) % MOD

                    # 3. 현재 숫자를 seq2에 추가
                    ng2 = gcd(g2, x)
                    new_dp[g1][ng2] = (new_dp[g1][ng2] + cur) % MOD

            dp = new_dp  # 다음 숫자로 넘어감

        # 정답 계산: 두 GCD가 같고, 둘 다 비어있지 않은 경우(g != 0)를 모두 합산
        answer = 0
        for g in range(1, MAX_VAL + 1):
            answer = (answer + dp[g][g]) % MOD

        return answer