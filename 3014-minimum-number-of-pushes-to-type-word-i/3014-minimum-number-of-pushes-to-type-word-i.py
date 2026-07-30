class Solution:
    def minimumPushes(self, word: str) -> int:
        cnt = Counter(word)

        number = 0
        ans = 0

        for ch in sorted(cnt, reverse=True):
            number += 1
            ans += (number//8+1 - (1 if number%8 == 0 else 0)) * cnt[ch]
        
        return ans