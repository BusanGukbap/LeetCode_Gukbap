class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        s = set()

        n = len(digits)

        for i in range(n):
            if digits[i] == 0:
                continue
            for j in range(n):
                for k in range(n):
                    if i == j or j == k or k == i:
                        continue
                    if digits[k] & 1:
                        continue
                    temp = str(digits[i]) + str(digits[j]) + str(digits[k])
                    s.add(temp)
        # print(s)
        return len(s)