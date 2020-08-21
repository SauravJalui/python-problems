import unittest
from UniqueCharInString import Solution

obj = Solution()

class UniqueCharTests(unittest.TestCase):
        def test_1(self):
            """uniq_char('abcdre') returns True"""
            self.assertEqual(obj.uniq_char('abcdre'), True)
       
        def test_2(self):
            """uniq_char('abcdrA') returns True"""
            self.assertEqual(obj.uniq_char('abcdrA'), True)
        
        def test_3(self):
            """uniq_char('abcdrd') returns False"""
            self.assertEqual(obj.uniq_char('abcdrd'), False)

        def test_4(self):
            """uniq_char('abcdree') returns False"""
            self.assertEqual(obj.uniq_char('abcdree'), False)


if __name__ == '__main__':
    unittest.main()
