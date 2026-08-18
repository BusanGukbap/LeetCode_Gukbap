class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = Counter()

        for i in range(n - k + 1):
            sub = nums[i:i+k]

            for x in set(sub):
                cnt[x] += 1

        ans = -1
        for num, freq in cnt.items():
            if freq == 1:
                ans = max(ans, num)
        
        return ans