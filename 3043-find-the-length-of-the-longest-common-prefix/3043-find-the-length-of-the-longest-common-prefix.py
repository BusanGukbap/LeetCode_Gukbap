class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix = set()

        for num in arr1:
            a = str(num)
            n = len(a)
            for j in range(n):
                prefix.add(a[:n-j])
        
        ans = 0
        for num in arr2:
            b = str(num)
            n = len(b)
            for j in range(n):
                if b[:n-j] in prefix:
                    ans = max(ans, n-j)
                    break

        
        return ans