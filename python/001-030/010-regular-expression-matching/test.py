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

    def test_isMatch(self):
        expected = False
        actual = self.s.isMatch("aa","a")
        self.assertEqual(actual, expected)

        expected = True
        actual = self.s.isMatch("aa","aa")
        self.assertEqual(actual, expected)


        expected = False
        actual = self.s.isMatch("aaa","aa")
        self.assertEqual(actual, expected)


        expected = True
        actual = self.s.isMatch("aa", "a*")
        self.assertEqual(actual, expected)


        expected = True
        actual = self.s.isMatch("aa", ".*")
        self.assertEqual(actual, expected)


        expected = True
        actual = self.s.isMatch("ab", ".*")
        self.assertEqual(actual, expected)


        expected = True
        actual = self.s.isMatch("aab", "c*a*b")
        self.assertEqual(actual, expected)

        expected = False
        actual = self.s.isMatch("aaa", "ab*a")
        self.assertEqual(actual, expected)

        expected = True
        actual = self.s.isMatch("aaa", "a.a")
        self.assertEqual(actual, expected)

        expected = False
        actual = self.s.isMatch("ab", ".*c")
        self.assertEqual(actual, expected)

        expected = False
        actual = self.s.isMatch("abcd", "d*")
        self.assertEqual(actual, expected)

        expected = True
        actual = self.s.isMatch("baccbbcbcacacbbc", "c*.*b*c*ba*b*b*.a*")
        self.assertEqual(actual, expected)

# unittest.main()
if __name__ == '__main__':
    # unittest.main()
    # print os.getcwd()
    print ''
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSolutionFuncs)
    unittest.TextTestRunner(verbosity=2).run(suite)

