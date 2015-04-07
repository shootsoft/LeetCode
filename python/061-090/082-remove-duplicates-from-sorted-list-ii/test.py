__author__ = 'yinjun'


import unittest
import os
import imp

class TestSolutionFuncs(unittest.TestCase):

    def setUp(self):
        path = os.getcwd() + '/solution.py'
        so = imp.load_source('solution', path)
        self.s = so.Solution()

        common = os.path.dirname(os.path.dirname(os.getcwd())) + '/common/listnode.py'
        print common
        listnode = imp.load_source('listnode', common)
        self.listnode = listnode.ListNode(0)

    def test_deleteDuplicates(self):

        expected = [1, 2, 5]
        actualList = [1,2,3,3,4,4,5]

        actual = self.s.deleteDuplicates(self.listnode.fromList(actualList)).toList()
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
