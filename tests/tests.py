import sys
import os
sys.path.append(os.path.abspath('..'))

import puffin

test_path = os.path.abspath(os.path.dirname(__file__))

def test_render():
    test_file = os.path.join(test_path, 'test.txt')
    p = puffin.Puffin(test_file)
    data = p.render()
    assert('<h1>Test</h1>' in data)
    assert('This is some text' in data)

def test_render_to_file():
    #tests that Puffin objects render sensibly
    test_file = os.path.join(test_path, 'test.txt')
    p = puffin.Puffin(test_file)
    p.render_to_file()
    assert('test.html' in os.listdir('.'))
