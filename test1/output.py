import imp
import sys

def create_module():
    # just for the scope barrier
    MODULE = imp.new_module('helper1')
    def foo(x):
        return 2
    MODULE.foo = foo
    return MODULE
sys.modules['helper1'] = create_module()
del create_module

def create_module():
    # just for the scope barrier
    MODULE = imp.new_module('helper1')
    b = 3245

    #TODO maybe just do these with all locals?
    MODULE.b = b
    return MODULE
sys.modules['helper2'] = create_module()
del create_module

def create_module():
    # just for the scope barrier
    MODULE = imp.new_module('my_helper')
    def bar(x):
        return 5
    MODULE.bar = bar
    MODULE.a = 4
    return MODULE
sys.modules['helper3'] = create_module()
del create_module
import helper2 as my_helper

from helper1 import foo

print foo(1)
