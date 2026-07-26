from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # 가장 큰 세 수를 저장 (초기값은 매우 작은 값으로)
        max1 = max2 = max3 = -1001
        # 가장 작은 두 수를 저장 (초기값은 매우 큰 값으로)
        min1 = min2 = 1001

        for n in nums:
            # 1. 가장 큰 세 수 갱신
            if n > max1:
                max3, max2, max1 = max2, max1, n
            elif n > max2:
                max3, max2 = max2, n
            elif n > max3:
                max3 = n

            # 2. 가장 작은 두 수 갱신
            if n < min1:
                min2, min1 = min1, n
            elif n < min2:
                min2 = n

        # 위에서 구한 값들로 두 가지 경우를 비교
        return max(max1 * max2 * max3, max1 * min1 * min2)