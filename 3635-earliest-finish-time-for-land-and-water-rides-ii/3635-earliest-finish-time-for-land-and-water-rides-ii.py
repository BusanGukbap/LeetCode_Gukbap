from bisect import bisect_right
from math import inf

class Solution:
    def earliestFinishTime(self, landStartTime, landDuration, waterStartTime, waterDuration) -> int:
        def solve(start1, dur1, start2, dur2):
            finish1 = min(s + d for s, d in zip(start1, dur1))
            return min(max(s, finish1) + d for s, d in zip(start2, dur2))

        return min(
            solve(landStartTime, landDuration, waterStartTime, waterDuration),
            solve(waterStartTime, waterDuration, landStartTime, landDuration),
        )