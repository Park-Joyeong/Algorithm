import unittest
from . import p_876_middle_of_the_linked_list


class Test_876(unittest.TestCase):

    def setUp(self):
        self.p = p_876_middle_of_the_linked_list
        self.s = p_876_middle_of_the_linked_list.Solution()

    def test_case1(self):
        last = self.p.ListNode(val=5)
        node3 = self.p.ListNode(val=4, next=last)
        node2 = self.p.ListNode(val=3, next=node3)
        node1 = self.p.ListNode(val=2, next=node2)
        head = self.p.ListNode(val=1, next=node1)
        self.assertEqual(self.s.middleNode(head).val, 3)

    def test_case2(self):
        last = self.p.ListNode(val=6)
        node4 = self.p.ListNode(val=5, next=last)
        node3 = self.p.ListNode(val=4, next=node4)
        node2 = self.p.ListNode(val=3, next=node3)
        node1 = self.p.ListNode(val=2, next=node2)
        head = self.p.ListNode(val=1, next=node1)
        self.assertEqual(self.s.middleNode(head).val, 4)
