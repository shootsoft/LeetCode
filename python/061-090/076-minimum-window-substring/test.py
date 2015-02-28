__author__ = 'yinjun'


import unittest
import os
import imp

class TestSolutionFuncs(unittest.TestCase):

    def setUp(self):
        path = os.getcwd() + '/' + 'solution.py'
        so = imp.load_source('solution', path)
        self.s = so.Solution()

    def test_minWindow(self):

        expected = "aa"
        actual = self.s.minWindow("aa", "aa")
        self.assertEqual(actual, expected)

        expected = "a"
        actual = self.s.minWindow("ab", "a")
        self.assertEqual(actual, expected)

        expected = "BANC"
        actual = self.s.minWindow("ADOBECODEBANC", "ABC")
        self.assertEqual(actual, expected)

        expected = ""
        actual = self.s.minWindow("a", "ab")
        self.assertEqual(actual, expected)

        expected = ""
        actual = self.s.minWindow("a", "aa")
        self.assertEqual(actual, expected)




# unittest.main()
if __name__ == '__main__':
    # unittest.main()
    # print os.getcwd()
    print ''
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSolutionFuncs)
    unittest.TextTestRunner(verbosity=2).run(suite)
#
# s = Solution()
# A = [0,2, 2, 2,1]
# s.sortColors(A)
# print A
