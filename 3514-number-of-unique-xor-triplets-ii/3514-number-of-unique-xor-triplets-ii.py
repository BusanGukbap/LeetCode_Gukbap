class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        uniq = list(set(nums))
        
        dp = [set() for _ in range(4)]
        dp[0].add(0)  # 0개를 선택하면 XOR은 0
        
        for num in uniq:
            for k in range(3, 0, -1):  # 역순으로 갱신 (중복 사용 방지)
                for prev in list(dp[k - 1]):
                    dp[k].add(prev ^ num)
        
        # 1개 또는 3개를 선택한 결과의 합집합 크기
        return len(dp[1] | dp[3])