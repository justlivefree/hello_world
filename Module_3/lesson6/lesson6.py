import os
from os import listdir, getcwd, system
from os.path import isdir


def manager_file(_path):
    files = listdir(_path)
    for i in range(len(files)):
        print(f'{i + 1}. {files[i]}')

    try:
        _c = input('>>> ')
        if len(_c) > 3:
            cmd = _c.split(' ')
            if cmd[0] == 'cf':
                with open(cmd[1], 'w+') as f:
                    pass
                manager_file(getcwd())
            else:
                os.mkdir(_path + '/' + cmd[1])
                manager_file(getcwd())
        else:
            _c = int(_c)
            if _c == 0:
                new_path = _path.split('/')[:-1]
                manager_file('/'.join(new_path))
            if isdir(_path + '/' + files[_c - 1]):
                manager_file(_path + '/' + files[_c - 1])
            else:
                system('vim ' + files[_c - 1])
    except ValueError:
        print('ERROR')
        manager_file(getcwd())


manager_file(getcwd())
