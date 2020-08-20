import unittest
from FindMissingElement import Solution

obj = Solution()

class MissingElementTests(unittest.TestCase):
        def test_1(self):
            """finder([1,2,3,4,5,6,7], [3,7,2,1,4,6]) returns 5"""
            self.assertEqual(obj.finder([1,2,3,4,5,6,7], [3,7,2,1,4,6]), (5))

        def test_2(self):
            """finder([5,5,7,7], [5,7,7]) returns 5"""
            self.assertEqual(obj.finder([5,5,7,7], [5,7,7]), (5))


if __name__ == '__main__':
    unittest.main()
