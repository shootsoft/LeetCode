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

    def test_convertToTitle(self):
        expected = 'A'
        actual = self.s.convertToTitle(1)
        self.assertEqual(actual, expected)

        expected = 'Z'
        actual = self.s.convertToTitle(26)
        self.assertEqual(actual, expected)


        expected = 'AA'
        actual = self.s.convertToTitle(27)
        self.assertEqual(actual, expected)

        expected = 'AZ'
        actual = self.s.convertToTitle(52)
        self.assertEqual(actual, expected)


# unittest.main()
if __name__ == '__main__':
    # unittest.main()
    # print os.getcwd()
    print ''
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSolutionFuncs)
    unittest.TextTestRunner(verbosity=2).run(suite)

