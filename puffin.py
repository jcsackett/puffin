#!/usr/bin/env python
# encoding: utf-8
"""
puffin.py

written by j.c.sackett on 2.19.2009
"""
from optparse import OptionParser
import markdown2
import sys
import os

MAJOR = 0
MINOR = 1

"""
Useful actions:
-p --process [FILE] process a file
-p --process [DIRECTORY] process all files in the directory
-v --version get version number
"""

if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-p", "--process", action="store", type="string", dest="target")
    parser.add_option("-v", "--version", action="store_true", dest="version")
    (options, args) = parser.parse_args(sys.argv)
    
    if options.version:
        print "puffin publishing system %d.%d" % (MAJOR, MINOR)
        exit()
    elif options.target:
        files = list()
        if os.path.isfile(options.target):
            files.append(options.target)
        elif os.path.isdir(options.target):
            files.extend([os.path.join(options.target, o) for o in os.listdir(options.target)])
        files = [f for f in files if not os.path.isdir(f)]
        print "Processing %s..." % ", ".join(files)
        for f in files:
                
            directory, filename = os.path.split(f)
            try:
                os.mkdir(os.path.join(directory, 'posts'))
            except OSError:
                pass
            text = file(f).read()
            html = markdown2.markdown(text)
            outfile = os.path.join(directory, 'posts', filename)
            file(outfile, 'w').write(html)
    