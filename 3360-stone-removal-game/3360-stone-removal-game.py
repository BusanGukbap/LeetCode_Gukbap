class Solution:
    def canAliceWin(self, n: int) -> bool:
        stones = 10
        alice = False
        while n >= stones:
            n -= stones
            stones -= 1
            alice ^= True
        
        return alice

        