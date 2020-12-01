import unittest
from fan import Fan
from ipmimsg import IpmiMsg

class FanTest(unittest.TestCase):
    def testParams(self):
        """ test these parameters should return the required ipmimsg
        """
        pass
        # Fan auto no longer return IpmiMsg object, it will depend model to perform action.
        # msg= Fan().getAction("auto")
        # self.assertTrue(msg == IpmiMsg(Fan.AUTO_CMD))

        # wrong parameter should return the document object.
    def testWrongParams(self):
        doc = Fan().getAction("hello")
        self.assertEqual(doc, Fan.__doc__)
        doc = Fan().getAction("")
        self.assertEqual(doc, Fan.__doc__)


    def testSupported(self):
        """ Me class should return a listed of supported commands.
        """
        support = Fan().supported_cmds
        self.assertIn('duty', support)
        self.assertIn('auto', support)

if __name__ == '__main__':
    unittest.main()