from typing import List
from math import gcd

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        n = len(coins)
        
        subsets = []
        for mask in range(1, 1 << n):
            lcm_val = 1
            bits = 0
            for i in range(n):
                if mask & (1 << i):
                    lcm_val = lcm_val // gcd(lcm_val, coins[i]) * coins[i]
                    bits += 1
            
            sign = 1 if bits % 2 == 1 else -1
            subsets.append((lcm_val, sign))
        
        min_coin = min(coins)
        low = 1
        high = min_coin * k
    
        while low < high:
            mid = (low + high) // 2
            count = 0
            
            for lcm_val, sign in subsets:
                count += sign * (mid // lcm_val)
            
            if count >= k:
                high = mid
            else:
                low = mid + 1
                
        return low