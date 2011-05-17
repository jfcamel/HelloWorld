#!/bin/env python
# -*- coding: utf-8 -*-

#------------------------------------------------------------------------------
# Copyright 2011 ~ jun fujita (fujita.jun@gmail.com)
#------------------------------------------------------------------------------

import sys
from ctypes import *

libc = None
if sys.platform == 'linux2':
    libc = CDLL("libc.so.6")
else:
    libc = cdll.msvcrt

def printf(s):
    libc.printf(s)

if __name__ == '__main__':
    printf("Hello World!\n")
