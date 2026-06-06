from typing import Tuple, Dict

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        return self._count_up_to(num2) - self._count_up_to(num1 - 1)

    def _transition(self, state: Tuple[int, int, int], digit: int) -> Tuple[Tuple[int, int, int], int]:
        length, prev2, prev1 = state
        if length == 0 and digit == 0:
            return (0, 10, 10), 0
        if length == 0:
            return (1, 10, digit), 0
        if length == 1:
            return (2, prev1, digit), 0

        wave = int((prev2 < prev1 and prev1 > digit) or (prev2 > prev1 and prev1 < digit))
        return (2, prev1, digit), wave

    def _count_up_to(self, n: int) -> int:
        if n <= 0:
            return 0

        digits = list(map(int, str(n)))
        m = len(digits)
        states = [(length, prev2, prev1) for length in range(3) for prev2 in range(11) for prev1 in range(11)]

        tail = [{state: (1, 0) for state in states}]
        for remaining in range(1, m+1):
            layer: Dict[Tuple[int, int, int], Tuple[int, int]] = {}
            prev_layer = tail[remaining - 1]
            for state in states:
                count = 0
                waves = 0

                for digit in range(10):
                    next_state, wave = self._transition(state, digit)
                    child_count, child_waves = prev_layer[next_state]
                    count += child_count
                    waves += child_waves + wave * child_count
                layer[state] = (count, waves)
            tail.append(layer)

        answer = 0
        prefix_waves = 0
        state = (0, 10, 10)

        for pos, actual in enumerate(digits):
            remaining = m - pos - 1
            for digit in range(actual):
                next_state, wave = self._transition(state, digit)
                suffix_count, suffix_waves = tail[remaining][next_state]
                answer += (prefix_waves + wave) * suffix_count + suffix_waves
            
            state, wave = self._transition(state, actual)
            prefix_waves += wave
        
        return answer + prefix_waves