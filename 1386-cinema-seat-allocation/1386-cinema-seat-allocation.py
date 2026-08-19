from collections import defaultdict
from typing import List

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        LEFT = 0b00001111
        MID = 0b00111100
        RIGHT = 0b11110000

        seats = defaultdict(int)
        for row, col in reservedSeats:
            if 2 <= col <= 9:
                seats[row] |= 1 << (col - 2)

        answer = (n - len(seats)) * 2

        for mask in seats.values():
            if (mask & LEFT) == 0 and (mask & RIGHT) == 0:
                answer += 2
            elif (mask & LEFT) == 0 or (mask & RIGHT) == 0:
                answer += 1
            elif (mask & MID) == 0:
                answer += 1

        return answer