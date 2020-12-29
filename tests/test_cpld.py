import unittest
from cpld import Cpld
from ipmimsg import IpmiMsg

class MeTest(unittest.TestCase):
    def testParams(self):
        """ test these parameters should return the required ipmimsg
        """
        msg= Cpld().getAction("fw")
        self.assertTrue(msg == IpmiMsg([0x30, 0x17, 3]))
        msg= Cpld().getAction("cksum")
        self.assertTrue(msg == IpmiMsg([0x30, 0x17, 1]))
        msg= Cpld().getAction("id")
        self.assertTrue(msg == IpmiMsg([0x30, 0x17, 2]))

        # wrong parameter should return the document object.
    def testWrongParams(self):
        doc = Cpld().getAction("hello")
        self.assertEqual(doc, Cpld.__doc__)
        doc = Cpld().getAction("")
        self.assertEqual(doc, Cpld.__doc__)


    def testSupported(self):
        """ Me class should return a listed of supported commands.
        """
        support = Cpld().getSupportCmds()
        self.assertIn('fw', support)
        self.assertIn('cksum', support)
        self.assertIn('id', support)
        self.assertNotIn('hello', support)     # hello is definitely not a command

if __name__ == '__main__':
    unittest.main()