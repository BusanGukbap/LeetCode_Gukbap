class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # 1. 값 기준 정렬
        pairs = sorted([(nums[i], i) for i in range(n)])
        
        # 2. 원래 인덱스 -> 정렬된 위치 매핑
        order = [0] * n
        for pos, (val, idx) in enumerate(pairs):
            order[idx] = pos
        
        # 3. 한 번에 갈 수 있는 최대 위치 (투 포인터)
        rightmost = [0] * n
        r = 0
        for l in range(n):
            if r < l:
                r = l
            while r + 1 < n and pairs[r + 1][0] - pairs[l][0] <= maxDiff:
                r += 1
            rightmost[l] = r
        
        # 4. 이진 리프팅 테이블
        LOG = (n).bit_length()
        up = [[0] * n for _ in range(LOG)]
        for i in range(n):
            up[0][i] = rightmost[i]
        
        for k in range(1, LOG):
            for i in range(n):
                up[k][i] = up[k-1][up[k-1][i]]
        
        # 5. 쿼리 처리
        ans = []
        for u, v in queries:
            u, v = order[u], order[v]
            if u > v:
                u, v = v, u
            
            if u == v:
                ans.append(0)
                continue
            
            dist = 0
            cur = u
            
            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < v:
                    dist += (1 << k)
                    cur = up[k][cur]
            
            if up[0][cur] >= v:
                ans.append(dist + 1)
            else:
                ans.append(-1)
        
        return ans