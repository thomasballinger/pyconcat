pyconcat
--------

Tries to concatenate several python modules into a single script.
Does this by creating module-like objects and sticking them in sys.modules
for each module found to be a dependency.

As done as I'm going to make it for a while, since acheived the goal
of concatenating my [toy bittorrent
client](https://github.com/thomasballinger/bittorrent).

*This is obviously a terrible idea! Don't use this!*

Instructions:

* clone repo (`git clone https://github.com/thomasballinger/pyconcat.git`)

* navigate to the script with dependencies you're trying to concatenate

* run `python ../../../pyconcat/pyconcat.py yourscriptwithdependencies.py alltogether.py`

See also
--------

pybreeder [https://github.com/pagekite/PyBreeder] by @BjarniRunar looks like a
more sensible way to go about this, instead of building fake modules.

Notes
-----

* Going to start with my files, then packages and dependencies, maybe down the
line compiled stuff? 

I bet this would really screw up a lot of things; pickle comes to mind
immediately

* todo: check out modulefinder and modulegraph for the dependencies step

We need to do some __name__ modifying, and some other things probably too

First: figure out dependencies

We could do this the same way (just dynamically recreate all the modules from
big strings) or we could do something more interesting

Don't conditionally import things! Or at least don't do it after code that would
fail in a parser
