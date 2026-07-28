from collections import Counter

class Solution:
    def smallestPalindrome(self, s: str) -> str:
        cnt = Counter(s)
        half = ""
        mid = ""

        for ch in sorted(cnt):
            if cnt[ch] % 2 == 1:
                mid = ch
            half += ch * (cnt[ch]//2)
        
        ans = half + mid + half[::-1]
        return ans