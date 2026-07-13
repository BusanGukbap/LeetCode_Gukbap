import math

class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"

        a = int(math.log10(low))+1
        b = int(math.log10(high))+1

        # print(a, b)

        ans = list()

        for i in range(10):
            for j in range(i+a, i+b+1):
                if j >= 10:
                    break
                
                num = int(s[i:j])
                # print(num)
                if low <= num <= high:
                    ans.append(num)
        
        return sorted(ans)