class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        
        for i in range(n, 101):
            a = i%10
            b = i//10
            
            temp = a*b if b != 0 else a

            if temp % t == 0:
                return i
        
        return 0