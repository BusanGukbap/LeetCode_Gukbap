class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        uniq = list(set(nums))

        n = len(uniq)

        dp = [set() for _ in range(4)]
        dp[0].add(0)

        for num in uniq:
            for k in range(3, 0, -1):
                for prev in list(dp[k-1]):
                    dp[k].add(prev ^ num)
        
        return len(dp[1] | dp[3])