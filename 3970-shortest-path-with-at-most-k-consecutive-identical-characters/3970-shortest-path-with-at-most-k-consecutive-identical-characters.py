class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
        
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]
        
        dist[0][1] = 0
        pq = [(0, 0, 1)]
        
        while pq:
            cost, u, cnt = heapq.heappop(pq)
            
            if cost > dist[u][cnt]:
                continue

            if u == n - 1:
                return cost
            
            for v, w in graph[u]:
                if labels[u] == labels[v]:
                    next_cnt = cnt + 1
                else:
                    next_cnt = 1
                
                if next_cnt > k:
                    continue
                
                next_cost = cost + w
                
                if next_cost < dist[v][next_cnt]:
                    dist[v][next_cnt] = next_cost
                    heapq.heappush(pq, (next_cost, v, next_cnt))
        
        return -1