__author__ = 'yinjun'


import unittest
import os
import imp

class TestSolutionFuncs(unittest.TestCase):

    def setUp(self):
        path = os.getcwd() + '/' + 'solution.py'
        so = imp.load_source('solution', path)
        self.s = so.Solution()

    def test_removeDuplicates(self):

        expected = [1,1,2,2,3]
        actual = [1,1, 1,2, 2, 3]
        actualLen = self.s.removeDuplicates(actual)
        self.assertEqual(actualLen, len(expected))
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
