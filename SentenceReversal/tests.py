import unittest
from SentenceReversal import Solution

obj = Solution()

class SentenceReversalTests(unittest.TestCase):
        def test_1(self):
            """rev_words('    space before') returns ('before space')"""
            self.assertEqual(obj.rev_words('    space before'),('before space'))

        def test_2(self):
            """rev_words('space after     '),'after space'"""
            self.assertEqual(obj.rev_words('space after     '),('after space'))

        def test_3(self):
            """rev_words('space after     '),'after space'"""
            self.assertEqual(obj.rev_words('   Hello John    how are you   '),('you are how John Hello'))


if __name__ == '__main__':
    unittest.main()
