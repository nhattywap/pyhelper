from importlib import import_module, reload
import argparse

def get_module_attrs(module):
    try:
        return (attr for attr in dir(reload(import_module(module))))
    except Exception as e:
        print('There is no module named %s' %(module))
        return False

def bind_attr_(module):
    dirs = get_module_attrs(module)
    if dirs:
        return ('%s.%s' % (module, attr) for attr in dirs)
    else:
        return False

def get_help_(module):
    help_this = []
    gen_attrs = bind_attr_(module)
    if gen_attrs:
        for attr in gen_attrs:
            help_this.append(attr)
        
        def print_():
            for i, attr in enumerate(help_this):
                print(i, attr)

        flag = True
        while flag:
            t = input('print table: ')
            if t == 'y':
                print_()
                
            index = int(input('INDEX:-> '))
            if index ==  -1:
                flag = False
            else:
                help(help_this[index])
    else:
        return False

def main():
    while True:
        mod = input('MODULE:-> ')
        get_help_(mod)
        stop = input('STOP:-> ')
        if stop == 'y':
            break
    
if __name__=='__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('-mh')
    args = vars(ap.parse_args())

    if 'mh' in args.keys():
        val = args['mh']
        get_help_(val)

