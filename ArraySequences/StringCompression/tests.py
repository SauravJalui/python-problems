import unittest
from StringCompression import Solution

obj = Solution()

class StringCompressionTests(unittest.TestCase):
        def test_1(self):
            """compress('') Empty string returns ('') Empty String"""
            self.assertEqual(obj.compress(''), (''))

        def test_2(self):
            """compress('AABBCC') returns ('A2B2C2')"""
            self.assertEqual(obj.compress('AABBCC'), ('A2B2C2'))

        def test_3(self):
            """compress('AAABCCDDDDD') returns ('A3B1C2D5')"""
            self.assertEqual(obj.compress('AAABCCDDDDD'), ('A3B1C2D5'))

        def test_4(self):
            """compress('AAABCCccDDDDD') returns ('A3B1C2c2D3d1D1')"""
            self.assertEqual(obj.compress('AAABCCccDDDdD'), ('A3B1C2c2D3d1D1'))


if __name__ == '__main__':
    unittest.main()
