from typing import List
from collections import deque

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)
        
        suspicious = [False] * n
        q = deque([k])
        suspicious[k] = True
        
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                if not suspicious[nxt]:
                    suspicious[nxt] = True
                    q.append(nxt)
        
        for u, v in invocations:
            if not suspicious[u] and suspicious[v]:
                return list(range(n))
    
        return [i for i in range(n) if not suspicious[i]]