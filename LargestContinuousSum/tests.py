import unittest
from LargestContinuousSum import Solution

obj = Solution()

class LargestContinuousSumTests(unittest.TestCase):
        def test_1(self):
            """large_cont_sum([1,2,-1,3,4,10,10,-10,-1]) returns 29"""
            self.assertEqual(obj.large_cont_sum([1,2,-1,3,4,10,10,-10,-1]), (29))

        def test_2(self):
            """large_cont_sum([1,2,-1,3,4,-1]) returns 9"""
            self.assertEqual(obj.large_cont_sum([1,2,-1,3,4,-1]),(9))


if __name__ == '__main__':
    unittest.main()
