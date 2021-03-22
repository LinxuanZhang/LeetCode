# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if not head:
            return None
        cur, pre = head, None
        for i in range(left, 1, -1):
            pre, cur = cur, cur.next
        tail, con = cur, pre # pointer for final connection
        for i in range(right-left+1):
            third = cur.next
            cur.next = pre
            pre = cur
            cur = third
        if con:
            con.next = pre
        else:
            head = pre
        tail.next = cur
        return head
