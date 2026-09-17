class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)
        min_len = [float('inf')] * n
        ans = float('inf')
        
        left = 0
        current_sum = 0
        
        for right in range(n):
            current_sum += arr[right]
            
            while current_sum > target:
                current_sum -= arr[left]
                left += 1
                
            if current_sum == target:
                cur_len = right - left + 1
                
                if left > 0 and min_len[left - 1] != float('inf'):
                    ans = min(ans, min_len[left - 1] + cur_len)
                
                min_len[right] = min(min_len[right - 1] if right > 0 else float('inf'), cur_len)
            else:
                min_len[right] = min_len[right - 1] if right > 0 else float('inf')
                
        return ans if ans != float('inf') else -1