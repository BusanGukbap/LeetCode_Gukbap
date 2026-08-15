class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        max_len = 0
        count = dict()
        left = 0

        for right, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1

            while count[ch] > 2:
                count[s[left]] -= 1
                left += 1


            max_len = max(max_len, right - left + 1)


        return max_len