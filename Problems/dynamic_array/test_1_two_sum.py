import unittest
from . import q_1_two_sum


class Test_1(unittest.TestCase):

    def test_case1(self):
        s = q_1_two_sum.Solution()
        self.assertEqual(s.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_case2(self):
        s = q_1_two_sum.Solution()
        self.assertEqual(s.twoSum([3, 2, 4], 6), [1, 2])

    def test_case3(self):
        s = q_1_two_sum.Solution()
        self.assertEqual(s.twoSum([3, 3], 6), [0, 1])
