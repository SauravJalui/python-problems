import unittest
from AnagramCheck import Solution

obj = Solution()

class AnagramTests(unittest.TestCase):

    def test_1(self):
        """anagram('dog','god') returns True"""
        self.assertEqual(obj.anagram('dog','god'), True)

    def test_2(self):
        """anagram(''clint eastwood','old west action') returns True"""
        self.assertEqual(obj.anagram('clint eastwood','old west action'), True)


if __name__ == '__main__':
    unittest.main()
