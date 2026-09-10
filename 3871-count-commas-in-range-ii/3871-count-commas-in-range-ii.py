class Solution:
    def countCommas(self, n: int) -> int:
        ans = 0

        index = 3
        while n > (10 ** index - 1):
            ans += max(0, n - (10 ** index - 1))
            index += 3

        return ans