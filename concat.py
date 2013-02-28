


#TODO if '__globals__' in module text, freak out
#TODO if encodings are different, fail

import modulefinder

def concatenate(filename, method=None, output=None):
    finder = modulefinder.ModuleFinder(debug=0)
    finder.run_script(filename)
    # for module finder to work it has to be able to run the file and get everything it will need
    finder.report()
    print finder.modules

    #TODO figure out which modules are stdlib and which aren't
    #TODO figure out the order in which modules need to be loaded
    #TODO whine about globals

    build_main_file_with_module_objects(filename, finder.modules, output)

def build_main_file_with_module_objects(mainfile, modules, output):

    def module_template(name, filename):
        print name, filename
        indented_module_code = '\n'.join(
            ['    '+line if line else ''
                for line in open(filename).read().split('\n')])
        s = """
def create_module(): # just for the scope barrier
    MODULE = imp.new_module('{name}')
{indented_module_code}
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
    for name, module in modules.iteritems():
        main += module_template(name, module.__file__)
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
    parser.add_argument('-o', '--output', default='main.py')
    parser.add_argument('-x', '--executable', action='store_true', help='make new script executable')

    args = parser.parse_args()
    #args = parser.parse_args(['./main.py', 'output.py'])

    concatenate(args.file, method=args.method, output=args.output)
