import unittest
from . import q_1290_convert_binary_number_in_a_linked_list_to_integer


class Test_1290(unittest.TestCase):

    def test_case1(self):
        s = q_1290_convert_binary_number_in_a_linked_list_to_integer.Solution()
        node2 = q_1290_convert_binary_number_in_a_linked_list_to_integer.ListNode(
            val=1)
        node1 = q_1290_convert_binary_number_in_a_linked_list_to_integer.ListNode(
            val=0, next=node2)
        node0 = q_1290_convert_binary_number_in_a_linked_list_to_integer.ListNode(
            val=1, next=node1)

        self.assertEqual(s.getDecimalValue(node0), 5)

    def test_case2(self):
        s = q_1290_convert_binary_number_in_a_linked_list_to_integer.Solution()
        node0 = q_1290_convert_binary_number_in_a_linked_list_to_integer.ListNode(
            val=0)

        self.assertEqual(s.getDecimalValue(node0), 0)

    def test_case3(self):
        s = q_1290_convert_binary_number_in_a_linked_list_to_integer.Solution()
        node0 = q_1290_convert_binary_number_in_a_linked_list_to_integer.ListNode(
            val=1)
        self.assertEqual(s.getDecimalValue(node0), 1)

    def test_case4(self):
        s = q_1290_convert_binary_number_in_a_linked_list_to_integer.Solution()
        node14 = q_1290_convert_binary_number_in_a_linked_list_to_integer.ListNode(
            val=0)
        node13 = q_1290_convert_binary_number_in_a_linked_list_to_integer.ListNode(
            val=0, next=node14)
        node12 = q_1290_convert_binary_number_in_a_linked_list_to_integer.ListNode(
            val=0, next=node13)
        node11 = q_1290_convert_binary_number_in_a_linked_list_to_integer.ListNode(
            val=0, next=node12)
        node10 = q_1290_convert_binary_number_in_a_linked_list_to_integer.ListNode(
            val=0, next=node11)

        node9 = q_1290_convert_binary_number_in_a_linked_list_to_integer.ListNode(
            val=0, next=node10)
        node8 = q_1290_convert_binary_number_in_a_linked_list_to_integer.ListNode(
            val=1, next=node9)
        node7 = q_1290_convert_binary_number_in_a_linked_list_to_integer.ListNode(
            val=1, next=node8)
        node6 = q_1290_convert_binary_number_in_a_linked_list_to_integer.ListNode(
            val=1, next=node7)
        node5 = q_1290_convert_binary_number_in_a_linked_list_to_integer.ListNode(
            val=0, next=node6)

        node4 = q_1290_convert_binary_number_in_a_linked_list_to_integer.ListNode(
            val=0, next=node5)
        node3 = q_1290_convert_binary_number_in_a_linked_list_to_integer.ListNode(
            val=1, next=node4)
        node2 = q_1290_convert_binary_number_in_a_linked_list_to_integer.ListNode(
            val=0, next=node3)
        node1 = q_1290_convert_binary_number_in_a_linked_list_to_integer.ListNode(
            val=0, next=node2)
        node0 = q_1290_convert_binary_number_in_a_linked_list_to_integer.ListNode(
            val=1, next=node1)

        self.assertEqual(s.getDecimalValue(node0), 18880)

    def test_case5(self):
        s = q_1290_convert_binary_number_in_a_linked_list_to_integer.Solution()
        node1 = q_1290_convert_binary_number_in_a_linked_list_to_integer.ListNode(
            val=0)
        node0 = q_1290_convert_binary_number_in_a_linked_list_to_integer.ListNode(
            val=0, next=node1)

        self.assertEqual(s.getDecimalValue(node0), 0)
