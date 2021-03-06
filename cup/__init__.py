#!/bin/env python
# -*- coding: utf-8 -*
"""
    @author Guannan Ma
"""

import sys

# { Check Env
if sys.version_info < (2, 6):
    raise ImportError(
        'cup needs to be run on python 2.6 and above.'
    )
# End Check-Env }


from cup import log

from cup import decorators
from cup import err

from cup import mail
from cup import net
from cup import version
if sys.platform.startswith('linux'):
    from cup import shell
from cup import timeplus as time
# pylint: disable=W0404
# For backwards compatity
from cup import timeplus
from cup import util
from cup import unittest

try:
    from cup import bidu
except ImportError:
    pass
from cup import res
from cup import oper
from cup import thirdp
from cup import platforms

try:
    # pylint: disable=W0104
    bidu
    __all__ = [
        'err', 'net', 'bidu', 'log', 'mail', 'shell', 'time',
        'util', 'unittest', 'decorators', 'thirdp', 'platforms'
    ]
# pylint:disable=W0702
except:
    __all__ = [
        'err', 'net', 'log', 'mail', 'shell', 'time',
        'util', 'unittest', 'decorators', 'thirdp', 'platforms'
    ]

# vi:set tw=0 ts=4 sw=4 nowrap fdm=indent
