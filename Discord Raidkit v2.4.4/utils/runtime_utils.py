"""
Discord Raidkit v2.4.4
the-cult-of-integral

Last modified: 2023-11-04 20:22
"""

import os
import sys


def is_running_as_executable():
    _, ext = os.path.splitext(sys.executable if getattr(sys, 'frozen', False) else sys.argv[0])
    return ext.lower() in ('.exe', '')
