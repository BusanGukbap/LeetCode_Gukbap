import math

class Solution:
    def dfs(self, g: List[List[int]], cur_node: int, past_node: int) -> int:
        max_depth = 0
        for next_node in g[cur_node]:
            if next_node == past_node:
                continue
            max_depth = max(max_depth, self.dfs(g, next_node, cur_node) + 1)
        return max_depth


    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        # def combination(depth: int) -> int:
        #     modulo = 10**9+7
        #     ans = 0

        #     for i in range(1, depth+1, 2):
        #         ans = (ans + math.comb(depth, i)) % modulo

        #     return ans
        N = len(edges) + 1

        g = [[] for _ in range(N + 1)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        max_dep = self.dfs(g, 1, 0)

        return 2**(max_dep - 1) % (10**9+7)