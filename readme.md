uglify.py

name to be changed later probably - it doesn't obfuscate, it just tries to
concatenate.

This is obviously a terrible idea! Don't use this!

check out modulefinder and modulegraph for the dependencies step

Combines python files into one long file.

Going to start with my files, then packages and dependencies, maybe down the
line compiled stuff

I bet this would really screw up a lot of things; pickle comes to mind
immediately

We need to do some __name__ modifying, and some other things probably too

First: figure out dependencies


We could do this the same way (just dynamically recreate all the modules from
big strings) or we could do something more interesting
