import unittest
from ipmimsg import IpmiMsg
from nic import Nic

class MeTest(unittest.TestCase):
    def testParams(self):
        """ test these parameters should return the required ipmimsg
        """
        msg= Nic().getAction("dedicate")
        self.assertTrue(msg == IpmiMsg([0xc, 1, 1, 0xff, 0]))
        msg= Nic().getAction("lom-share")
        self.assertTrue(msg == IpmiMsg([0xc, 1, 1, 0xff, 1]))
        msg= Nic().getAction("mezz-share0")
        self.assertTrue(msg == IpmiMsg([0xc, 1, 1, 0xff, 2]))
        msg= Nic().getAction("mezz-share1")
        self.assertTrue(msg == IpmiMsg([0xc, 1, 1, 0xff, 3]))

        # wrong parameter should return the document object.
    def testWrongParams(self):
        doc = Nic().getAction("hello")
        self.assertEqual(doc, Nic.__doc__)
        doc = Nic().getAction("")
        self.assertEqual(doc, Nic.__doc__)


    def testSupported(self):
        """ Me class should return a listed of supported commands.
        """
        support = Nic().supported_cmds
        self.assertIn("dedicate", support)
        self.assertIn("lom-share", support)
        self.assertIn("mezz-share0", support)
        self.assertIn("mezz-share1", support)
        self.assertNotIn('hello', support)     # hello is definitely not a command

if __name__ == '__main__':
    unittest.main()