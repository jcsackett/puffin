#!/usr/bin/env python
# encoding: utf-8
"""
puffin.py

written by j.c.sackett on 2.19.2009
"""
from optparse import OptionParser
from jinja2 import Environment, PackageLoader

import sys
import os
import markdown2
import subprocess


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
        self.write_path = file_path.replace(dest, '').replace('//', '/').replace('.txt', '.html')
    
def init_posts(output_dir):
    try:
        os.mkdir('posts')
    except OSError:
        print 'Post directory already exists. Use -r or --rebuild to force overwrite.'

def get_files(dest):
    files = []
    for root, ds, fs in os.walk(dest):
        for name in fs:
            if name[0] == ".": continue
            path = os.path.join(root, name)
            f = file_pair(path,dest)
            files.append(f)
    return files

def process_files(file_list, output_dir):
    print 'Processing %s...' % [f.read_path for f in file_list]
    for f in file_list:    
        os.path.split(f.read_path)
        text = file(f.read_path).read()
        html = markdown2.markdown(text)
        html = create_detail(html)
        outfile = os.path.join(output_dir, f.write_path)
        new_folder = os.path.split(outfile)[0]
        try:
            os.mkdir(new_folder)
        except OSError:
            pass
        file(outfile, 'w').write(html)

def create_detail(post):
    template = ENV.get_template('detail.jinja')
    return template.render(**{'post':post})
    

def print_version():
    print "puffin publishing system %d.%d" % (MAJOR, MINOR)
    exit()
    
def preview(f):
    browser = subprocess.Popen('open /Applications/Safari.app "%s"' % f, shell=True)
    exit()
    
if __name__ == '__main__':
    output_dir = 'posts'
    
    parser = OptionParser()
    parser.add_option("-p", "--preview", action="store", type="string", dest="preview")
    parser.add_option("-v", "--version", action="store_true", dest="version")
    parser.add_option("-r", "--rebuild", action="store_true", dest="rebuild")
    parser.add_option("-o", "--output-path", action="store", type="string", dest="output_dir")
    (options, args) = parser.parse_args(sys.argv)
    
    if options.output_dir: output_dir = options.output_dir
    if options.version:    print_version()
    if options.preview:    preview(options.preview)
    if options.rebuild:    os.rmdir(output_dir)
    
    target = args[1]
    print target
    init_posts(output_dir)
    file_list = get_files(target)
    process_files(file_list, output_dir)
    
        