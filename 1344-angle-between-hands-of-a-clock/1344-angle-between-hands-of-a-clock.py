class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle1 = 0

        angle1 += (hour % 12) * 30
        angle1 += (minutes)* 0.5
        
        angle2 = minutes * 6

        ans = (angle1-angle2)%360
        return min(ans, 360-ans)