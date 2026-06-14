# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # 1. slow/fast로 중간 지점 찾기
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. 뒤 절반 뒤집기  (slow부터 끝까지)
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
            
        # 3. 앞에서부터 + 뒤에서부터 동시에 이동하며 최대합 구하기
        ans = 0
        left, right = head, prev
        while right:
            ans = max(ans, left.val + right.val)
            left = left.next
            right = right.next

        return ans