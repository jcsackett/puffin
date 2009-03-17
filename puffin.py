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

def init_posts():
    try:
        os.mkdir('posts')
    except OSError:
        pass

def get_files(dest):
    files = list()
    if os.path.isfile(dest):
        files.append(dest)
    elif os.path.isdir(dest):
        files.extend([os.path.join(dest, o) for o in os.listdir(dest)])
    return [f for f in files if not os.path.isdir(f)]

def process_files(file_list):
    print 'Processing %s...' % files
    for f in files:    
        directory, filename = os.path.split(f)
        text = file(f).read()
        html = markdown2.markdown(text)
        outfile = os.path.join(directory, 'posts', filename)
        file(outfile, 'w').write(html)

def print_version():
    print "puffin publishing system %d.%d" % (MAJOR, MINOR)
    exit()
    
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-p", "--process", action="store", type="string", dest="target")
    parser.add_option("-v", "--version", action="store_true", dest="version")
    parser.add_optioN("-s", "--start", action="store_true", dest="start")
    (options, args) = parser.parse_args(sys.argv)
    
    if options.version: print_version()
    elif options.start: init_posts()
    elif options.target:
        file_list = get_files(options.target)
        process_files(file_list)