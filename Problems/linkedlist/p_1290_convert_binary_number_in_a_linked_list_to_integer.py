# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Sol.1
# class Solution:
#     def getDecimalValue(self, head: ListNode) -> int:
#         list = []
#         result = 0
#         while True:
#             list.append(head.val)
#             if head.next == None:
#                 break
#             head = head.next
#         for idx, val in enumerate(list):
#             result = result + val * 2 ** (len(list)-1-idx)
#         return result

# Sol.2
# class Solution:
#     def getDecimalValue(self, head: ListNode) -> int:
#         num = head.val
#         while head.next:
#             num = num * 2 + head.next.val
#             head = head.next
#         return num

# Sol.3
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = head.val
        while head.next:
            num = (num << 1) | head.next.val
            head = head.next
        return num
