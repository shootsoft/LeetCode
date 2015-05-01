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

    def test_threeSumClosest(self):
        expected = 2
        actual = self.s.threeSumClosest([-1,2,1,-4], 1)
        self.assertEqual(actual, expected)

        expected = 3
        actual = self.s.threeSumClosest([0,1,2], 3)


# unittest.main()
if __name__ == '__main__':
    # unittest.main()
    # print os.getcwd()
    print ''
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSolutionFuncs)
    unittest.TextTestRunner(verbosity=2).run(suite)

