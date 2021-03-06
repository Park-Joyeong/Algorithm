import unittest
from . import q_1929_concatenation_of_array


class Test_1929(unittest.TestCase):

    def test_case1(self):
        s = q_1929_concatenation_of_array.Solution()
        self.assertEqual(s.getConcatenation(
            [1, 2, 1]), [1, 2, 1, 1, 2, 1])

    def test_case2(self):
        s = q_1929_concatenation_of_array.Solution()
        self.assertEqual(s.getConcatenation(
            [1, 3, 2, 1]), [1, 3, 2, 1, 1, 3, 2, 1])
