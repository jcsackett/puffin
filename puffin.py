#!/usr/bin/env python
# encoding: utf-8
"""
puffin.py

written by j.c.sackett on 2.19.2009
"""
from optparse import OptionParser

import sys
import os
import subprocess

MAJOR = 0
MINOR = 2

def get_files(dest):
    files = []
    for root, ds, fs in os.walk(dest):
        for name in fs:
            if name[0] == ".": continue
            path = os.path.join(root, name)
            f = post(path,dest)
            files.append(f)
    return files
    
def init_posts(output_dir):
    try:
        os.mkdir(output_dir)
    except OSError:
        print 'Post directory already exists. Use -r or --rebuild to force overwrite.'


def process_files(file_list, output_dir):
    print 'Processing markdown for %s...' % [f.read_path for f in file_list]
    for f in file_list:    
        os.path.split(f.read_path)
        text = file(f.read_path).read()
        f.content = markdown2.markdown(text)
        
def create_page(post):
    print post.content
    template = ENV.get_template('detail.jinja')
    html = template.render(post=post)
    outfile = os.path.join(output_dir, post.write_path)
    new_folder = os.path.split(outfile)[0]
    try:
        os.mkdir(new_folder)
    except OSError:
        pass
    file(outfile, 'w').write(html)
    
    
def create_frontpage(post_list, top_dir):
    template = ENV.get_template('frontpage.jinja')
    html = template.render(posts=post_list)
    file(os.path.join(top_dir, 'index.html'), 'w').write(html)
         

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
    create_frontpage(file_list, output_dir)
    [create_page(f) for f in file_list]
    
    
        