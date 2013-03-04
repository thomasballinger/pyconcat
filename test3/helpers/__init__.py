print 'running init now'
import sys
print sys.modules.keys()
print 'importing HelperError'
from .helpererror import HelperError
HelperError
print sys.modules.keys()
print 'done importing HelperError'

print 'name in an __init__.py:', __name__
print 'path on an __init__.py:', __path__

def foo(x):
    return x
