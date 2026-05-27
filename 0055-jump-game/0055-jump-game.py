class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        ans = False

        q = list()
        q.append(0)

        visited = [False]*N
        visited[0] = True

        while q:
            cur = q.pop()

            if cur == N-1:
                break

            for i in range(nums[cur]):
                if cur + i + 1 >= N:
                    break
                if visited[cur + i + 1] == True:
                    continue
                
                q.append(cur + i + 1)
                visited[cur + i + 1] = True

        if visited[N-1] == True:
            return True
        return False