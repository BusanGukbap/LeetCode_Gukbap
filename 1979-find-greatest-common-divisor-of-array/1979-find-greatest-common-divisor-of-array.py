import math

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        a = min(nums)
        b = max(nums)

        return math.gcd(a, b)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna