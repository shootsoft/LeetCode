__author__ = 'yinjun'

import unittest
import os
import imp


class TestSolutionFuncs(unittest.TestCase):
    def setUp(self):
        path = os.getcwd() + '/solution.py'
        so = imp.load_source('solution', path)
        self.s = so.Solution()

        # common = os.path.dirname(os.path.dirname(os.getcwd())) + '/common/listnode.py'
        #print common
        #listnode = imp.load_source('listnode', common)
        #self.listnode = listnode.ListNode(0)

    def test_divide(self):
        expected = 	2147483647
        actual = self.s.divide(	-2147483648, -1)
        self.assertEqual(actual, expected)

        expected = 	1073741823
        actual = self.s.divide(	2147483647, 2)
        self.assertEqual(actual, expected)

        expected = 	-1
        actual = self.s.divide(	-1, 1)
        self.assertEqual(actual, expected)

        expected = 	-2147483648
        actual = self.s.divide(	-2147483648, 1)
        self.assertEqual(actual, expected)


# unittest.main()
if __name__ == '__main__':
    # unittest.main()
    # print os.getcwd()
    print ''
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSolutionFuncs)
    unittest.TextTestRunner(verbosity=2).run(suite)

