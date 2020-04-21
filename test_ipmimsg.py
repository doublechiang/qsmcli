import unittest
from ipmimsg import IpmiMsg

class IpmiMsgTest(unittest.TestCase):

    def testFormat(self):

        """ Bridge and channel and raw command should be translate be string.
        """
        str = IpmiMsg([2, 1, 1], 5, 3).format()
        self.assertEqual(str, "-t 0x5 -b 0x3 raw 0x2 0x1 0x1 ")
        str = IpmiMsg([2, 1, 1, 5], 11, 10).format()
        self.assertEqual(str, "-t 0xb -b 0xa raw 0x2 0x1 0x1 0x5 ")

    def testEqual(self):
        self.assertTrue(IpmiMsg([1, 1]) == IpmiMsg([1, 1]))
        self.assertFalse(IpmiMsg([1, 1]) == IpmiMsg([2, 1]))
        self.assertTrue(IpmiMsg([1, 1], 3, 5) == IpmiMsg([1, 1], 3, 5))
        self.assertFalse(IpmiMsg([1, 1], 3, 5) == IpmiMsg([1, 1], 4, 5))
        self.assertFalse(IpmiMsg([1, 1], 3, 5) == IpmiMsg([1, 1], 3, 6))



if __name__ == '__main__':
    unittest.main()