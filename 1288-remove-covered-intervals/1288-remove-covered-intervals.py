class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        
        ans = 0

        for i in range(n):
            a, b = intervals[i]

            for j in range(n):
                if i == j:
                    continue
                    
                c, d = intervals[j]

                if (c <= a and b <= d):
                    ans += 1
                    break
        
        return n-ans