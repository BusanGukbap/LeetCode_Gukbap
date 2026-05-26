class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        d = dict()
        
        large = 0
        small = 0

        for a in word:
            if 'A' <= a <= 'Z':
                large |= 1<<(ord(a)-ord('A'))
            elif 'a' <= a <= 'z':
                small |= 1<<(ord(a)-ord('a'))
            
        ans = large & small

        cnt = 0
        while ans:
            cnt += ans & 1
            ans = ans >> 1
        
        return cnt