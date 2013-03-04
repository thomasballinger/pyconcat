import os
from glob import glob
import difflib


test_folders = glob('test*')
test_folders.remove('test.py')

for test in test_folders:
    os.system('cd %s; python ../concat.py main.py testoutput.py' % test)
    expected = open(test+'/testoutput.py').read()
    actual = open(test+'/expectedoutput.py').read()
    if expected == actual:
        print test, 'passed'
    else:
        print test, 'failed'
        for line in difflib.unified_diff(expected.split('\n'), actual.split('\n'), fromfile='expected', tofile='actual'):
            print line
