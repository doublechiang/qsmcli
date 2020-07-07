import os,sys

import logging
import qsmcli.qsmcli

logging.basicConfig(level=logging.WARNING)
qsmcli.qsmcli.Qsmcli().run()
