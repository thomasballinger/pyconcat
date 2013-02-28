import imp
import sys

def create_module():
    # just for the scope barrier
    MODULE = imp.new_module('helper1')
    def foo(x):
        return 2
    MODULE.foo = foo
sys.modules['helper1'] = create_module()
del create_module

def create_module():
    # just for the scope barrier
    MODULE = imp.new_module('helper1')
    b = 3245

    #TODO maybe just do these with all locals?
    MODULE.b = b
sys.modules['helper2'] = create_module()
del create_module

import helper2 as my_helper

from helper1 import foo

print foo(1)
