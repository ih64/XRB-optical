"""module pyrafglobals.py -- widely used PyRAF constants and objects

pyrafDir        Directory with these Pyraf programs
_use_ecl        Flag to turn on ECL mode in PyRAF

This is defined so it is safe to say 'from pyrafglobals import *'

$Id: pyrafglobals.py 1463 2011-06-24 22:58:30Z stsci_embray $

Broken out from irafglobals.py which was signed "R. White, 2000 January 5"
"""
from __future__ import division # confidence high

import os, sys
_os = os
_sys = sys
del os, sys

_use_ecl = _os.environ.get("PYRAF_USE_ECL", False)

# -----------------------------------------------------
# pyrafDir is directory containing this script
# -----------------------------------------------------
if __name__ == "__main__":
    thisfile = _sys.argv[0]
else:
    thisfile = __file__
# follow links to get to the real filename
while _os.path.islink(thisfile):
    thisfile = _os.readlink(thisfile)
pyrafDir = _os.path.dirname(thisfile)
del thisfile

from stsci.tools.irafglobals import userWorkingHome
if not pyrafDir: pyrafDir = userWorkingHome
# change relative directory paths to absolute and normalize path
pyrafDir = _os.path.normpath(_os.path.join(userWorkingHome, pyrafDir))
del userWorkingHome
