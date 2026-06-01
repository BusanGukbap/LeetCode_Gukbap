class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort()
        ans = 0
        n = len(cost)
        while n:
            if n:
                ans += cost[-1]
                cost.pop()
                n -= 1
            if n:
                ans += cost[-1]
                cost.pop()
                n -= 1
            if n:
                cost.pop()
                n -= 1
        
        return ans
                