class Solution:
    def maxProduct(self, n: int) -> int:
        ans = 0

        n = str(n)
        digits = list()
        for i in range(len(n)):
            for j in range(i+1, len(n)):
                ans = max(ans, int(n[i]) * int(n[j]))
        
        return ans