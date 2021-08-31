import unittest
from . import _1920_build_array_from_permutation


class Test_1920(unittest.TestCase):

    def test_case1(self):
        s = _1920_build_array_from_permutation.Solution()
        self.assertEqual(s.buildArray([0, 2, 1, 5, 3, 4]), [0, 1, 2, 4, 5, 3])

    def test_case2(self):
        s = _1920_build_array_from_permutation.Solution()
        self.assertEqual(s.buildArray([5, 0, 1, 2, 3, 4]), [4, 5, 0, 1, 2, 3])
