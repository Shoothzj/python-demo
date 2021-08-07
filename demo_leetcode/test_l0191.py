from unittest import TestCase
from l0191 import Solution


class TestSolution(TestCase):
    def test_hamming_weight(self):
        solution = Solution()
        hamming_weight = solution.hammingWeight(0x00000000000000000000000000001011)
        print("result is ", hamming_weight)
