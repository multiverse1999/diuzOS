# SPDX-License-Identifier: GPL-3.0 
'''*
   * diuz/version 0.2/fs.py
   *
   * Copyright (C) 2022 multiverse1999
   *
   * this file is file system
   *'''
def disk(operation: str, _disk: dict, args: dict):
    if operation == '''FCREATE''':
        _disk[args['''directory''']]['''file'''] = {'''1''': args['''desc'''], '''2''': '''FILE'''}
    elif operation == '''CONFCREATE''':
        _disk['''reg'''][args['''param''']] = {'''1''': args['''desc'''], '''2''': '''CONF'''}
    elif operation == '''RCREATE''':
        _disk[args['''directory''']] = {}
    elif operation == '''FREMOVE''':
        _disk[args['''directory''']][args['''file''']] = None
    elif operation == '''DRESET''':
        _disk = {'''c''': {}, '''reg''': {}}
_fs = {'''c''': {}, '''reg''': {}}

def dexp():
    global _fs
    print('''help:\n''')
    print('''file mk (directory name)/(file) (content) - create file\n''')
    print('''file rm (directory name)/(file name) - remove file\n''')
    print('''dir mk (directory name) - create directory''')
    while True:
        try:
            action = input('''dfs> ''')
            sa = action.split()
            if sa[0] == '''file''':
                if sa[1] == '''mk''':
                    ss = sa[2].replace('''/''', ''' ''')
                    ss = ss.split()
                    disk('''FCREATE''', _fs, {'''file''': ss[1], '''directory''': ss[0], '''desc''': sa[3]})
                    print(f'''file {ss[1]} succesfully created!''')
                elif sa[1] == '''rm''':
                    sa = sa[2].replace('''/''', ''' ''')
                    sa = sa.split()
                    disk("FREMOVE", _fs, {'''file''': sa[1], '''directory''': sa[0]})
                    print(f'''file {sa[1]} succesfully removed!''')
            elif sa[0] == '''dir''':
                if sa[1] == '''mk''':
                    disk('''RCREATE''', _fs, {'''directory''': sa[2]})
                    print('''directory created!''')
            elif sa[0] == '''back''':
               print('''\n''')
               break
        except:
            pass
