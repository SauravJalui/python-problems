import unittest
from ArrayPairSum import Solution

obj = Solution()

class ArrayPairSumTests(unittest.TestCase):
        def test_1(self):
            """pair_sum([1,2,3,4], 5)) returns 2"""
            self.assertEqual(obj.pair_sum([1,2,3,4], 5), (2))

        def test_2(self):
            """pair_sum([1,2,3,4], 5)) returns 2"""
            self.assertEqual(obj.pair_sum([1,3,2,2], 4), (2))

    #test cases if we needed the pair of values instead
    # def test_1(self):
    #     """print(pair_sum([1,2,3,4], 5)) returns (2,3), (1,4)"""
    #     self.assertEqual(obj.pair_sum([1,2,3,4], 5), {(2,3), (1,4)})
   
    # def test_2(self):
    #     """print(pair_sum([1,3,2,2], 4)) returns (1,3), (2,2)"""
    #     self.assertEqual(obj.pair_sum([1,2,3,2], 4), {(1,3), (2,2)})


if __name__ == '__main__':
    unittest.main()
