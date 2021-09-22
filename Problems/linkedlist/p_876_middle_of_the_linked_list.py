from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# My approach
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         half_node = head
#         toggle = True
#         while head.next:
#             if toggle:
#                 half_node = half_node.next
#             head = head.next
#             toggle = not toggle
#         return half_node

# Leet solution
class Solution:
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
