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

    def test_titleToNumber(self):
        expected = 1
        actual = self.s.titleToNumber('A')
        self.assertEqual(actual, expected)

        expected = 26
        actual = self.s.titleToNumber('Z')
        self.assertEqual(actual, expected)


        expected = 27
        actual = self.s.titleToNumber('AA')
        self.assertEqual(actual, expected)

        expected = 52
        actual = self.s.titleToNumber('AZ')
        self.assertEqual(actual, expected)


# unittest.main()
if __name__ == '__main__':
    # unittest.main()
    # print os.getcwd()
    print ''
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSolutionFuncs)
    unittest.TextTestRunner(verbosity=2).run(suite)

