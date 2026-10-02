class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ans = list()

        def func(a: int, b: int, s: str):
            if a == 0 and b == 0:
                ans.append(s)
                return

            if a > 0:
                func(a-1, b, s+'(')
            if a < b:
                func(a, b-1, s+')')
            return
        func(n, n, "")
        return ans