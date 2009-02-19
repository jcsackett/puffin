#!/usr/bin/env python
# encoding: utf-8
"""
puffin.py

written by j.c.sackett on 2.19.2009
"""
from optparse import OptionParser
import markdown2
import sys

"""
Useful actions:
-p [FILE] process a file
-p [DIRECTORY] process all files in the directory
"""

if __name__ == '__main__':
    args = sys.argv
    parser = OptionParser()
    parser.add_option("-p", "--process", action="store", type="string", dest="target")
    
    (options, args) = parser.parse_args(args)
    
    print options.target