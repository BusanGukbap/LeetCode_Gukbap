class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        n = len(s)
        ans = True
        i = 0

        while i < n and ans == True:
            if s[i] in ['(', '[', '{']:
                stack.append(s[i])
            elif s[i] in [']', '}', ')'] and len(stack) == 0:
                ans = False
            elif s[i] == ')' and stack[-1] == '(':
                stack.pop()
            elif s[i] == '}' and stack[-1] == '{':
                stack.pop()
            elif s[i] == ']' and stack[-1] == '[':
                stack.pop()
            else:
                ans = False

            i += 1

        if len(stack):
            ans = False
        return ans