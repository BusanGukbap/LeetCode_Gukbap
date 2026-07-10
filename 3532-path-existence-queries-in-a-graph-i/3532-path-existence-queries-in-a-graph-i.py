class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        parent = list(range(n))


        def find(x : int) -> int:
            while x != parent[x]:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(a : int, b : int):
            ra = find(a)
            rb = find(b)
            if ra != rb:
                parent[rb] = ra

        for i in range(1, n):
            if nums[i] - nums[i-1] <= maxDiff:
                union(i-1, i)
        
        return [find(u) == find(v) for u, v in queries]