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


if __name__ == '__main__':
    unittest.main()