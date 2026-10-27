class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ans = []
        first_row = '.'*n
        ans.append(first_row)
        
        for i in range(1, m):
            temp = '#' * (n-1) + '.'
            ans.append(temp)
        return ans