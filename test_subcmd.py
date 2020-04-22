import unittest

from subcmd import SubCmd

class SubCmdTest(unittest.TestCase):
    def testComposeList(self):
        """ test helper function of Subcmd
        """
        self.assertEqual([1,2,3,4,5,6], SubCmd().composeList([1], 2, 3, 4, 5, 6))
        self.assertEqual([1,2,3,4,5,6], SubCmd().composeList([1, 2], 3, 4, 5, 6))
        self.assertEqual([1,2,3,4,5,6], SubCmd().composeList([1, 2], 3, [4, 5], 6))
        self.assertEqual([1,2,3,4], SubCmd().composeList(1, 2, 3, 4))

if __name__ == '__main__':
    unittest.main()