from typing import List
from functools import lru_cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        @lru_cache(maxsize=None)
        def dfs(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            
            take_left = nums[left] - dfs(left + 1, right)
            take_right = nums[right] - dfs(left, right - 1)
            
            return max(take_left, take_right)
        
        return dfs(0, n - 1) >= 0