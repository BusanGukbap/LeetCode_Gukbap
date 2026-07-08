MOD = 10**9 + 7
pow10 = [1] * 100001
for i in range(1, 100001):
    pow10[i] = pow10[i - 1] * 10 % MOD


class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        
        ## 0이 아닌 개수 -> 숫자 길이
        prefix_nonzero = [0] * (n + 1)
        ## 문제에서의 sum
        prefix_sum = [0] * (n + 1)
        ## 문제에서의 x
        prefix_x = [0] * (n + 1)


        ## prefix 계산
        for i, ch in enumerate(s):
            digit = int(ch)

            prefix_sum[i+1] = prefix_sum[i] + digit
            
            if digit != 0:
                prefix_nonzero[i + 1] = prefix_nonzero[i] + 1
                prefix_x[i + 1] = (prefix_x[i] * 10 + digit) % MOD
            else:
                prefix_nonzero[i + 1] = prefix_nonzero[i]
                prefix_x[i + 1] = prefix_x[i]



        ## 쿼리 계산
        ans = list()
        for l, r in queries:

            r += 1
            length = prefix_nonzero[r] - prefix_nonzero[l]
            x = (prefix_x[r] - prefix_x[l] * pow10[length]) % MOD

            sum = prefix_sum[r] - prefix_sum[l]

            ans.append(sum * x%MOD)

        return ans