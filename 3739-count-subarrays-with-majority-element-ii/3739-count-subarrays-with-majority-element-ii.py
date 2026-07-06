class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        bit = [0] * (2 * n + 5)
        offset = n + 2
        def add(idx: int) -> None:
            while idx < len(bit):
                bit[idx] += 1
                idx += idx & -idx
        def query(idx: int) -> int:
            res = 0
            while idx > 0:
                res += bit[idx]
                idx -= idx & -idx
            return res
        ans = 0
        pref = 0
        add(pref + offset)
        for x in nums:
            pref += 1 if x == target else -1
            idx = pref + offset
            ans += query(idx - 1)
            add(idx)
        return ans