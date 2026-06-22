class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        d = dict()
        d['b'] = 0
        d['a'] = 0
        d['l'] = 0
        d['n'] = 0
        d['o'] = 0

        for a in text:
            if a in ['b', 'a', 'l', 'o', 'n']:
                d[a] += 1

        return min(d['b'], d['a'], d['l']//2, d['n'], d['o']//2)