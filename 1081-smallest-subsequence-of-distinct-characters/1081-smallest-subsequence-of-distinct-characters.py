class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # 1. 각 문자의 마지막 등장 위치 저장
        last_occ = {c: i for i, c in enumerate(s)}
        
        stack = []      # 정답을 쌓을 스택
        visited = set() # 현재 스택에 포함된 문자들
        
        for i, c in enumerate(s):
            # 이미 정답에 포함된 문자는 건너뛰기
            if c in visited:
                continue
            
            # 스택의 top이 현재 문자보다 크고,
            # top 문자가 나중에 다시 등장한다면 pop
            while stack and stack[-1] > c and last_occ[stack[-1]] > i:
                visited.remove(stack.pop())
            
            # 현재 문자를 스택에 추가
            stack.append(c)
            visited.add(c)
        
        return ''.join(stack)