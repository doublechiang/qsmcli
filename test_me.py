import unittest
from me import Me
from ipmimsg import IpmiMsg

class MeTest(unittest.TestCase):
    def testParams(self):
        """ test these parameters should return the required ipmimsg
        """
        msg= Me().getAction("version")
        self.assertTrue(msg == IpmiMsg([6, 1], brdg=0x2c, chnl=6))
        msg = Me().getAction("cpu")
        self.assertTrue(msg == IpmiMsg([0x4, 0x2d, 0xbe], brdg=0x2c, chnl=6))
        msg = Me().getAction("dimm")
        self.assertTrue(msg == IpmiMsg([0x4, 0x2d, 0xc0], brdg=0x2c, chnl=6))
        msg = Me().getAction("io")
        self.assertTrue(msg == IpmiMsg([0x4, 0x2d, 0xbf], brdg=0x2c, chnl=6))

        # wrong parameter should return the document object.
    def testWrongParams(self):
        doc = Me().getAction("hello")
        self.assertEqual(doc, Me.__doc__)
        doc = Me().getAction("")
        self.assertEqual(doc, Me.__doc__)


    def testSupported(self):
        """ Me class should return a listed of supported commands.
        """
        support = Me().supported_cmds
        self.assertIn('version', support)
        self.assertIn('dimm', support)
        self.assertIn('cpu', support)
        self.assertIn('io', support)
        self.assertNotIn('hello', support)     # hello is definitely not a command

if __name__ == '__main__':
    unittest.main()