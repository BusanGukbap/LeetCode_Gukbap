from typing import List
from functools import lru_cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        @lru_cache(maxsize=None)
        def dfs(left: int, right: int) -> int:
            # 현재 플레이어가 nums[left:right+1]에서 얻을 수 있는 최대 점수 차이 반환
            if left == right:
                return nums[left]
            
            # 왼쪽 끝을 가져가는 경우
            take_left = nums[left] - dfs(left + 1, right)
            # 오른쪽 끝을 가져가는 경우
            take_right = nums[right] - dfs(left, right - 1)
            
            return max(take_left, take_right)
        
        return dfs(0, n - 1) >= 0