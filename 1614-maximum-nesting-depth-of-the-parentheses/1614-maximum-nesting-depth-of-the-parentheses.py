class Solution:
    def maxDepth(self, s: str) -> int:
        n = len(s)

        ans = 0
        cur_depth = 0
        for i in range(n):
            if s[i] == '(':
                cur_depth += 1
                ans = max(ans, cur_depth)
            
            elif s[i] == ')':
                cur_depth -= 1
            
        return ans