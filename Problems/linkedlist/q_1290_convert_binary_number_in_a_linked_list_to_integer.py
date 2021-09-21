# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        list = []
        result = 0
        while True:
            list.append(head.val)
            if head.next == None:
                break
            head = head.next
        for idx, val in enumerate(list):
            result = result + val * 2 ** (len(list)-1-idx)
        return result
