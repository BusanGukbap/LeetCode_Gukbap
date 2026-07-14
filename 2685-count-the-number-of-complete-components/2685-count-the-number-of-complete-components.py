class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]

        def find(x: int) -> int:
            while x != parents[x]:
                parents[x] = parents[parents[x]]
                x = parents[x]
            return x

        def union(a: int, b: int):
            ra = find(a)
            rb = find(b)

            if ra != rb:
                parents[rb] = ra


        for a, b in edges:
            union(a, b)

        node_count = defaultdict(int)
        edge_count = defaultdict(int)

        for i in range(n):
            node_count[find(i)] += 1
        for a, b in edges:
            edge_count[find(a)] += 1

        result = 0
        
        for root, m in node_count.items():
            if edge_count[find(root)] == m*(m-1)/2:
                result += 1
        
        return result