import heapq

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        # f[i]=1이면 i에 도달 가능, 0이면 i에 도달 불가능
        f, pre = [0] * n, [0] * n
        f[0] = 1
        
        for i in range(minJump):
            pre[i] = 1
        
        for i in range(minJump, n):
            left, right = i - maxJump, i-minJump

            if s[i] == "0":
                if left <= 0:
                    total = pre[right] - 0
                else:
                    total = pre[right] - pre[left-1]
                
                if total == 0:
                    f[i] = 0
                else:
                    f[i] = 1

            pre[i] = pre[i - 1] + f[i]
        return bool(f[n-1])

