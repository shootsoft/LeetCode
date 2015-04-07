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

    def test_twoSum(self):
        expected = (3, 5)
        actual = self.s.twoSum([-1, -2, -3, -4, -5], -8)
        self.assertEqual(actual, expected)

        expected = (2, 3)
        actual = self.s.twoSum([3,2,4], 6)
        self.assertEqual(actual, expected)


        expected = (1, 3)
        actual = self.s.twoSum([-3,4,3,90], 0)
        self.assertEqual(actual, expected)


# unittest.main()
if __name__ == '__main__':
    # unittest.main()
    # print os.getcwd()
    print ''
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSolutionFuncs)
    unittest.TextTestRunner(verbosity=2).run(suite)

