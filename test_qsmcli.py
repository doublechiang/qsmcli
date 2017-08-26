#!/usr/bin/env python3

import unittest
import argparse
from qsmcli import Qsmcli

class QsmcliTest(unittest.TestCase):

    def test_sdr(self):
        qsmcli= Qsmcli('dontcare sdr info'.split())
        self.assertTrue(qsmcli.args.sdr_sub)
        qsmcli= Qsmcli('dontcare sdr list'.split())
        self.assertTrue(qsmcli.args.sdr_sub)
        qsmcli= Qsmcli('dontcare sdr elist'.split())
        self.assertTrue(qsmcli.args.sdr_sub)

        ### check if invalid arguemnt will have error response.
        try:
            qsmcli= Qsmcli('dontcare sdr xxx'.split())
        except SystemExit:
            pass
        except Excetion as e:
            self.fail('Unexpected exception raised:', e)
        else:
            self.fail('ExpectedException not raised')

    def test_mac(self):
        qsmcli= Qsmcli('dontcare mac 0'.split())
        self.assertTrue(qsmcli.args.mac_sub)

        qsmcli= Qsmcli('dontcare mac 1'.split())
        self.assertTrue(qsmcli.args.mac_sub)

        qsmcli= Qsmcli('dontcare mac 2'.split())
        self.assertTrue(qsmcli.args.mac_sub)

        qsmcli= Qsmcli('dontcare mac 3'.split())
        self.assertTrue(qsmcli.args.mac_sub)

        qsmcli= Qsmcli('dontcare mac 4'.split())
        self.assertTrue(qsmcli.args.mac_sub)

        qsmcli= Qsmcli('dontcare mac 5'.split())
        self.assertTrue(qsmcli.args.mac_sub)

        try:
            qsmcli= Qsmcli('dontcare mac 6'.split())
            self.assertTrue(qsmcli.args.mac_sub)
        except SystemExit:
            pass
        else:
            self.fail('ExpectedException not raised')

        try:
            qsmcli= Qsmcli('dontcare mac'.split())
        except SystemExit:
            pass
        else:
            self.fail('ExpectedException not raised')

    def test_cpld(self):
        qsmcli= Qsmcli('dontcare cpld fw'.split())
        self.assertTrue(qsmcli.args.cpld_sub)
        qsmcli= Qsmcli('dontcare cpld cksum'.split())
        self.assertTrue(qsmcli.args.cpld_sub)
        qsmcli= Qsmcli('dontcare cpld id'.split())
        self.assertTrue(qsmcli.args.cpld_sub)

        try:
            qsmcli= Qsmcli('dontcare cpld'.split())
        except SystemExit:
            pass
        else:
            self.fail('ExpectedException not raised')

        try:
            qsmcli= Qsmcli('dontcare cpld xxx'.split())
        except SystemExit:
            pass
        else:
            self.fail('ExpectedException not raised')

    def test_sel(self):
        qsmcli= Qsmcli('dontcare sel info'.split())
        self.assertTrue(qsmcli.args.sel_sub)
        qsmcli= Qsmcli('dontcare sel list'.split())
        self.assertTrue(qsmcli.args.sel_sub)

        try:
            qsmcli= Qsmcli('dontcare sel'.split())
        except SystemExit:
            pass
        else:
            self.fail('ExpectedException not raised')

        try:
            qsmcli= Qsmcli('dontcare sel xxx'.split())
        except SystemExit:
            pass
        else:
            self.fail('ExpectedException not raised')

    def test_nic(self):
        qsmcli= Qsmcli('dontcare nic dedicate'.split())
        self.assertTrue(qsmcli.args.nic_sub)
        qsmcli= Qsmcli('dontcare nic lom-share'.split())
        self.assertTrue(qsmcli.args.nic_sub)
        qsmcli= Qsmcli('dontcare nic mezz-share0'.split())
        self.assertTrue(qsmcli.args.nic_sub)
        qsmcli= Qsmcli('dontcare nic mezz-share1'.split())
        self.assertTrue(qsmcli.args.nic_sub)

        try:
            qsmcli= Qsmcli('dontcare nic'.split())
        except SystemExit:
            pass
        else:
            self.fail('ExpectedException not raised')

        try:
            qsmcli= Qsmcli('dontcare nic xxx'.split())
        except SystemExit:
            pass
        else:
            self.fail('ExpectedException not raised')


    def test_ipmi(self):
        qsmcli= Qsmcli('dontcare ipmi mc info'.split())
        self.assertTrue(qsmcli.args.ipmi_sub)

    def setUp(self):
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
