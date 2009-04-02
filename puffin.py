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
from jinja2 import Environment, PackageLoader

MAJOR = 0
MINOR = 1

ENV = Environment(loader=PackageLoader('puffin', 'templates'))


"""
Useful actions:
-p --process [FILE] process a file
-p --process [DIRECTORY] process all files in the directory
-v --version get version number
"""
class file_pair:
    read_path = ''
    write_path = ''
    
    def __init__(self, file_path, dest):
        self.read_path = file_path
        self.write_path = file_path.replace(dest, '').replace('//', '/')
    
def init_posts():
    try:
        os.mkdir('posts')
    except OSError:
        print 'Post directory already exists.'

def get_files(dest):
    files = []
    for root, ds, fs in os.walk(dest):
        for name in fs:
            if name[0] == ".": continue
            path = os.path.join(root, name)
            f = file_pair(path,dest)
            files.append(f)
    return files

def process_files(file_list):
    print 'Processing %s...' % file_list
    for f in file_list:    
        os.path.split(f.read_path)
        text = file(f.read_path).read()
        html = markdown2.markdown(text)
        outfile = os.path.join('posts', f.write_path)
        new_folder = os.path.split(outfile)[0]
        try:
            os.mkdir(new_folder)
        except OSError:
            print "%s already exists; skipping creation." % new_folder
            pass
        file(outfile, 'w').write(html)

def create_detail(f):
    

def print_version():
    print "puffin publishing system %d.%d" % (MAJOR, MINOR)
    exit()
    
if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-p", "--process", action="store", type="string", dest="target")
    parser.add_option("-v", "--version", action="store_true", dest="version")
    parser.add_option("-s", "--start", action="store_true", dest="start")
    (options, args) = parser.parse_args(sys.argv)
    
    if options.version: print_version()
    elif options.start: init_posts()
    elif options.target:
        file_list = get_files(options.target)
        process_files(file_list)