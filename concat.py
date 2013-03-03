

#TODO if '__globals__' in module text, freak out
#TODO if encodings are different, fail

import sys

import py2depgraph

def get_deps_in_order(filename):
    def link_graph(depgraph):
        """Link graph so it really can be traversed the way I'm traversing it"""
        for key, depdict in depgraph.items():
            for depkey in depdict.keys():
                if depkey in depgraph:
                    depdict[depkey] = depgraph[depkey]

    mf = py2depgraph.mymf(debug=10, excludes=['unittest'])
    mf.run_script(filename)
    depgraph = mf._depgraph
    link_graph(depgraph)

    def mod_we_need(mod):
        if mod.__name__ in sys.builtin_module_names:
            return False
        if mod.__file__[-3:] == '.so':
            return False
        if 'site-packages' in mod.__file__:
            return True
        if '/lib/python' in mod.__file__:
            return False
        return True

    def leafgen(tree):
        for leaf in tree:
            mod = mf.modules[leaf]
            if not mod_we_need(mod) and not mod.__name__ == '__main__':
                continue  # we don't need __main__, but still want its dependecies
            if tree[leaf] == 1:
                yield mod
            else:
                for innerleaf in leafgen(tree[leaf]):
                    yield innerleaf
                if mod_we_need(mod) and mod.__name__ != '__main__':
                    yield mod

    def no_repeats(iterable):
        imported = []
        for k in iterable:
            if k in imported:
                pass
            else:
                imported.append(k)
                yield k

    return no_repeats(leafgen(depgraph))

def concatenate(filename, method=None, output=None):
    # for module finder to work it has to be able to run the file and get everything it will need
    dep_modules = get_deps_in_order(args.file)

    #TODO figure out which modules are stdlib and which aren't
    #TODO figure out the order in which modules need to be loaded
    #TODO whine about globals

    build_main_file_with_module_objects(filename, dep_modules, output)

def build_main_file_with_module_objects(mainfile, modules, output):

    def module_template(name, filename):
        print 'concatenating', name, filename
        indented_module_code = '\n'.join(
            ['    '+line if line else ''
                for line in open(filename).read().split('\n')])
        s = """
# code for module {name}
def create_module(): # just for the scope barrier
    import sys, imp
    MODULE = imp.new_module('{name}')
    __name__ = '{name}'
    # code from module
{indented_module_code}
    # autogenerated export and cleanup
    for k, v in locals().items():
        setattr(MODULE, k, v)
    return MODULE
sys.modules['{name}'] = create_module()
del create_module
""".format(name=name, indented_module_code=indented_module_code)
        return s

    main = '#Generated by concat.py\n'
    main += 'import imp\n'
    main += 'import sys\n'
    for module in modules:
        main += module_template(module.__name__, module.__file__)
    main += '#main file\n'
    main += open(mainfile).read()
    open(output, 'w').write(main)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    parser.add_argument('output', default='main.py')
    parser.add_argument('-m', '--method', choices=['correct', 'naive', 'nomodules'], default='naive',
            help='Technique to use for creating a single file (defaults to "naive")')
    parser.add_argument('-x', '--executable', action='store_true', help='make new script executable')

    args = parser.parse_args()
    #args = parser.parse_args(['./main.py', 'output.py'])

    concatenate(args.file, method=args.method, output=args.output)

