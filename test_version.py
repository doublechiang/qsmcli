import unittest
import io
from contextlib import redirect_stdout
from version import Version
from ipmimsg import IpmiMsg

class VersionTest(unittest.TestCase):
    def testFunc(self):
        """ calling Version get action should return an function.
            Execute that function should print out the version.
        """
        func= Version().getAction("")
        f = io.StringIO()
        with redirect_stdout(f):
            func("")
        out = f.getvalue().strip()
        self.assertEqual(Version.VERSION, out)

if __name__ == '__main__':
    unittest.main()