from collections import Counter
from math import factorial

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        freq = Counter(s)
        
        # 홀수 길이인 경우 가운데 문자를 찾고, 해당 문자의 빈도수를 1 줄임
        mid = ''
        for ch in list(freq.keys()):
            if freq[ch] % 2 == 1:
                mid = ch
                freq[ch] -= 1
            freq[ch] //= 2
        
        # 전체 가능한 회문의 개수 계산 (k를 초과하면 조기 종료)
        total = self._count_permutations(freq, sum(freq.values()), k)
        if total < k:
            return ""
        
        # 왼쪽 절반의 길이
        half_len = n // 2
        
        # k번째 왼쪽 절반을 탐욕적으로 구성
        half = []
        remaining = half_len
        for _ in range(half_len):
            for ch in sorted(freq.keys()):
                if freq[ch] == 0:
                    continue
                # 이 문자를 현재 자리에 배치
                freq[ch] -= 1
                # 남은 자리로 만들 수 있는 순열의 개수 계산
                cnt = self._count_permutations(freq, remaining - 1, k)
                if cnt >= k:
                    half.append(ch)
                    break
                else:
                    # 이 문자로 시작하는 모든 순열을 건너뜀
                    k -= cnt
                    freq[ch] += 1
            else:
                # 적절한 문자를 찾지 못한 경우 (문제 조건상 발생하지 않음)
                return ""
            remaining -= 1
        
        # 완성된 왼쪽 절반과 그 역순, 그리고 가운데 문자를 결합
        left = ''.join(half)
        right = left[::-1]
        return left + mid + right
    
    def _count_permutations(self, freq: dict, length: int, cap: int) -> int:
        """
        주어진 빈도수로 만들 수 있는 서로 다른 순열의 개수를 계산.
        cap을 초과하면 cap을 반환하여 오버플로우를 방지.
        """
        res = 1
        remaining = length
        for cnt in freq.values():
            if cnt == 0:
                continue
            # combinations(remaining, cnt)를 계산하여 누적 곱
            res *= self._comb(remaining, cnt, cap)
            if res >= cap:
                return cap
            remaining -= cnt
        return res
    
    def _comb(self, n: int, r: int, cap: int) -> int:
        """
        조합 C(n, r)을 계산. cap을 초과하면 cap을 반환.
        """
        if r > n - r:
            r = n - r
        res = 1
        for i in range(1, r + 1):
            res = res * (n - r + i) // i
            if res >= cap:
                return cap
        return res