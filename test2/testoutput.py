#Generated by concat.py
import imp
import sys

def create_module(): # code for module helpers.helper1
    import sys, imp
    MODULE = imp.new_module('helpers.helper1')
    __name__ = 'helpers.helper1'
    # code from module
    a = 4
    def foo(x):
        return x + 1

    # autogenerated export and cleanup
    for k, v in locals().items():
        setattr(MODULE, k, v)
    return MODULE
sys.modules['helpers.helper1'] = create_module(); del create_module

def create_module(): # code for module helpers
    import sys, imp
    MODULE = imp.new_module('helpers')
    __name__ = 'helpers'
    # code from module

    # autogenerated export and cleanup
    for k, v in locals().items():
        setattr(MODULE, k, v)
    return MODULE
sys.modules['helpers'] = create_module(); del create_module
#main file
import helpers.helper1
print helpers.helper1.foo