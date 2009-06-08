'''
post.py
copyright 2009 j.c.sackett

Defines a post object which contains the file information of the base text file and
converts it into an html post.
'''
from jinja2 import Environment, PackageLoader
import markdown2
import os

ENV = Environment(loader=PackageLoader('puffin', 'templates'))

class post:
    def __init__(self, file_path, dest):
        self.read, self.write = self.build_paths(file_path)
        self.title = self.make_title(file_path)
        self.content = 
    
    def build_paths(self, file_path):
        r = file_path
        w = file_path.replace(dest, '').replace('//', '/').replace('.txt', '.html')d 
        return r,w
    
    def make_title(self, file_path):
        return os.path.split(file_path)[-1].split('.')[0].replace('_', ' ')
    
    def make_url(self):
        if self.write_path.startswith('/'):
            return self.write_path[1:]
        else:
            return self.write_path
    
    def build_page(self):
        pass

