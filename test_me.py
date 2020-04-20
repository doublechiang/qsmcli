import unittest
from me import Me

class MeTest(unittest.TestCase):
    def testParams(self):
        """ test these parameter should not have exception generate
        """
        Me("version")
        Me("cpu")
        Me("dimm")
        Me("io")

    def testWrongParameter(self):
        Me("heee")._validate_arg()

if __name__ == '__main__':
    unittest.main()