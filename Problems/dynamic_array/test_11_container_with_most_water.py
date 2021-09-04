import unittest
from . import q_11_container_with_most_water


class Test_11(unittest.TestCase):

    def test_case1(self):
        s = q_11_container_with_most_water.Solution()
        self.assertEqual(s.maxArea(
            [1, 8, 6, 2, 5, 4, 8, 3, 7]), 49)

    def test_case2(self):
        s = q_11_container_with_most_water.Solution()
        self.assertEqual(s.maxArea(
            [1, 1]), 1)

    def test_case3(self):
        s = q_11_container_with_most_water.Solution()
        self.assertEqual(s.maxArea(
            [4, 3, 2, 1, 4]), 16)

    def test_case4(self):
        s = q_11_container_with_most_water.Solution()
        self.assertEqual(s.maxArea(
            [1, 2, 1]), 2)
