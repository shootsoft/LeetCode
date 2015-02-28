import unittest
import os
import imp

class TestSolutionFuncs(unittest.TestCase):

    def setUp(self):
        path = os.getcwd() + '/' + 'solution.py'
        so = imp.load_source('solution', path)
        self.s = so.Solution()

    def test_sortColors(self):
        expected = [0, 1, 2, 2, 2]
        actual = [0, 2, 2, 2, 1]
        self.s.sortColors(actual)
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
