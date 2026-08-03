class Solution:
    def minimumPushes(self, word: str) -> int:
        frequencies = sorted(Counter(word).values(), reverse=True)

        answer = 0
        
        for i, freq in enumerate(frequencies):
            pushes = i//8 + 1
            answer += pushes * freq

        return answer
            