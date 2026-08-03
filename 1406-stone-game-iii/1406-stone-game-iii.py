from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
        dp_i1 = 0
        dp_i2 = 0
        dp_i3 = 0
        
        for i in range(n - 1, -1, -1):
            best = stoneValue[i] - dp_i1
            
            if i + 1 < n:
                best = max(best, stoneValue[i] + stoneValue[i+1] - dp_i2)
            
            if i + 2 < n:
                best = max(best, stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp_i3)
            
            dp_i3, dp_i2, dp_i1 = dp_i2, dp_i1, best
        
        if dp_i1 > 0:
            return "Alice"
        elif dp_i1 < 0:
            return "Bob"
        else:
            return "Tie"