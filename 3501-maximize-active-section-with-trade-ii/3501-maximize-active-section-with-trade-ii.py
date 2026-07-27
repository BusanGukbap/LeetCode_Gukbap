import bisect

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total_ones = s.count('1')
        
        # 1. 0 블록 추출
        zero_runs = []
        i = 0
        while i < n:
            if s[i] == '0':
                start = i
                while i < n and s[i] == '0':
                    i += 1
                zero_runs.append((start, i - 1))
            else:
                i += 1
        
        # 2. 인접한 두 0 블록을 하나의 pair로 묶음
        pairs = []  # (L1, R1, L2, R2, gain)
        for k in range(len(zero_runs) - 1):
            L1, R1 = zero_runs[k]
            L2, R2 = zero_runs[k + 1]
            gain = (R1 - L1 + 1) + (R2 - L2 + 1)
            pairs.append((L1, R1, L2, R2, gain))
        
        num_pairs = len(pairs)
        if num_pairs == 0:
            return [total_ones] * len(queries)
        
        # 3. Sparse Table 구축 (pair의 gain에 대한 구간 최대값)
        K = num_pairs.bit_length()
        st = [[0] * K for _ in range(num_pairs)]
        for j in range(num_pairs):
            st[j][0] = pairs[j][4]
        
        for j in range(1, K):
            for idx in range(num_pairs - (1 << j) + 1):
                st[idx][j] = max(st[idx][j-1], st[idx + (1 << (j-1))][j-1])
        
        def query_st(L: int, R: int) -> int:
            if L > R:
                return 0
            j = (R - L + 1).bit_length() - 1
            return max(st[L][j], st[R - (1 << j) + 1][j])
        
        # 4. 이진 탐색을 위한 배열
        R1_list = [p[1] for p in pairs]   # 첫 블록의 끝
        L2_list = [p[2] for p in pairs]   # 두 블록의 시작
        
        ans = []
        for l, r in queries:
            # 쿼리 범위에 걸리는 pair 인덱스 찾기
            first_k = bisect.bisect_left(R1_list, l)
            last_k = bisect.bisect_right(L2_list, r) - 1
            
            if first_k > last_k:
                ans.append(total_ones)
                continue
            
            best_gain = 0
            
            if first_k == last_k:
                # pair가 1개만 포함된 경우
                L1, R1, L2, R2, _ = pairs[first_k]
                gain = (R1 - max(L1, l) + 1) + (min(R2, r) - L2 + 1)
                best_gain = max(best_gain, gain)
            else:
                # 첫 번째 pair 처리 (첫 블록이 잘릴 수 있음)
                L1, R1, L2, R2, _ = pairs[first_k]
                gain1 = (R1 - max(L1, l) + 1) + (min(R2, r) - L2 + 1)
                best_gain = max(best_gain, gain1)
                
                # 마지막 pair 처리 (마지막 블록이 잘릴 수 있음)
                L1, R1, L2, R2, _ = pairs[last_k]
                gain2 = (R1 - max(L1, l) + 1) + (min(R2, r) - L2 + 1)
                best_gain = max(best_gain, gain2)
                
                # 중간에 완전히 포함된 pair들 (Sparse Table로 O(1) 조회)
                if first_k + 1 <= last_k - 1:
                    best_gain = max(best_gain, query_st(first_k + 1, last_k - 1))
            
            ans.append(total_ones + best_gain)
        
        return ans