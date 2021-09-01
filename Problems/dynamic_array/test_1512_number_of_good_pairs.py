import unittest
from . import q_1512_number_of_good_pairs


class Test_1512(unittest.TestCase):

    def test_case1(self):
        s = q_1512_number_of_good_pairs.Solution()
        self.assertEqual(s.numIdenticalPairs(
            [1, 2, 3, 1, 1, 3]), 4)

    def test_case2(self):
        s = q_1512_number_of_good_pairs.Solution()
        self.assertEqual(s.numIdenticalPairs(
            [1, 1, 1, 1]), 6)

    def test_case3(self):
        s = q_1512_number_of_good_pairs.Solution()
        self.assertEqual(s.numIdenticalPairs(
            [1, 2, 3]), 0)
