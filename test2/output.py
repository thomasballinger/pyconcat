#Generated by concat.py
import imp
import sys

# code for module helpers
def create_module(): # just for the scope barrier
    MODULE = imp.new_module('helpers')
    __name__ = 'helpers'
    # code from module

    # autogenerated export and cleanup
    for k, v in locals().items():
        setattr(MODULE, k, v)
    return MODULE
sys.modules['helpers'] = create_module()
del create_module

#main file
import helpers

print helpers.helper1.foo