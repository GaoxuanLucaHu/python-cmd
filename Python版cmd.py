# Visit https://www.lddgo.net/string/pyc-compile-decompile for more information
# Version : Python 3.10

import os
import sys
import subprocess
import datetime

print('Python cmd [version 0.4.2], developed by Python.')
print('Welcome to use this terminal, developed by Python.')
print('Unreliable studio development, all rights reserved.')
print(' ')
os.chdir('C:\\')
path = os.getcwd()


def help():
    print(
        'HELP 查看帮助。\nCD 进入某目录。\nMD 创建目录。\nDEL 删除文件。\nVER 版本信息\nEXIT 退出\nTREE 以图形界面查看指定目录下的所有目录和文件。（会报错）\nDIR 查看当前目录下的文件和目录\nSTART 打开应用程序或文件。')


def dir(directory):
    items = os.listdir(directory)
    for item in items:
        item_path = os.path.join(directory, item)
        size = os.path.getsize(item_path)
        modified_time = os.path.getmtime(item_path)
        modified_time_string = str(datetime.datetime.fromtimestamp(modified_time))
        if os.path.isfile(item_path):
            item_type = '<文件>'
        elif os.path.isdir(item_path):
            item_type = '<目录>'
        print(f'''{item:<20} {size:<10} {modified_time_string} {item_type}''')


def tree(directory, indent=('',)):
    items = os.listdir(directory)
    for index, item in enumerate(items):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            prefix = '├── '
        elif os.path.isdir(item_path):
            prefix = '└── '
        print(indent + prefix + item)
        if os.path.isdir(item_path):
            if index == len(items) - 1:
                new_indent = indent + '    '
            else:
                new_indent = indent + '│   '
            tree(item_path, new_indent)


def cd():
    if user[3:] != '..':
        cd_path = user[3:]
        cd_path_new = path + '\\' + cd_path
        if os.path.exists(cd_path_new) == True:
            os.chdir(cd_path_new)
            path = os.getcwd()
            return None
        None('系统找不到指定的路径。')
        return None
    if None[3:] == '.':
        print(path + '>')
        return None

    def GenMuLuJianCe():
        root_dir = os.path.dirname(path)
        return os.path.isdir(root_dir)

    if GenMuLuJianCe():
        print('已是根目录')
        return None
    back_cd_path = None.path.dirname(path)
    os.chdir(back_cd_path)
    path = os.getcwd()


def delete_file_and_dir():
    del_file_name = user[4:]
    del_file_name_other = path + '\\' + del_file_name
    if os.path.exists(del_file_name_other) == True:
        print('不要在C盘根目录和系统文件夹里删东西！会报错！')
        Q_1 = input('会删除此文件/文件夹！是否继续？（删除：Y，不删除：N）:')
        if Q_1 == 'Y' or Q_1 == 'y':
            os.remove(del_file_name_other)
            print('成功删除。（别怪我没提醒你哦）')
            return None
        if None == 'N' or Q_1 == 'n':
            return None
        None('输入错误！')
        continue
    print('系统找不到指定的文件/文件夹。')


def Make_dir():
    create_dir_name = user[3:]
    os.mkdir(create_dir_name)


def start():
    Start_App = user[6:]
    Start_App_with_Path = path + '\\' + Start_App
    if os.path.exists(Start_App_with_Path) == True:
        subprocess.run(Start_App_with_Path)
        return None
    None('系统找不到指定的文件。')


user = input(path + '>')
if user.startswith('del'):
    del_file_name = user[4:]
    del_file_name_other = path + '\\' + del_file_name
    if os.path.exists(del_file_name_other) == True:
        print('不要在C盘根目录和系统文件夹里删东西！会报错！')
        Q_1 = input('会删除此文件/文件夹！是否继续？（删除：Y，不删除：N）:')
        if Q_1 == 'Y' or Q_1 == 'y':
            os.remove(del_file_name_other)
            print('成功删除。（别怪我没提醒你哦）')
        elif Q_1 == 'N' or Q_1 == 'n':
            pass
        else:
            print('输入错误！')
        continue
    print('系统找不到指定的文件/文件夹。')
elif user == 'help':
    help()
elif user.startswith('md'):
    Make_dir()
elif user == 'ver':
    print('Python cmd [version 0.4.2]')
    continue
if user.startswith('cd'):
    if user[3:] != '..':
        cd_path = user[3:]
        cd_path_new = path + '\\' + cd_path
        if os.path.exists(cd_path_new) == True:
            os.chdir(cd_path_new)
            path = os.getcwd()
        else:
            print('系统找不到指定的路径。')
    elif user[3:] == '.':
        print(path + '>')
    elif path == 'C:\\':
        print('已是根目录')
        continue
    back_cd_path = os.path.dirname(path)
    os.chdir(back_cd_path)
    path = os.getcwd()
elif user == 'exit':
    sys.exit()
elif user.startswith('start'):
    start()
elif user == 'dir':
    dir(path)
elif user == 'C:':
    if os.path.exists('C:\\') == True:
        if path != 'C:\\':
            os.chdir('C:\\')
            path = os.getcwd()
        else:
            print('你已经在这个驱动器里了。')
        continue
    print('系统找不到指定的路径：', format(user))
elif user == 'tree':
    print('使用会遇到拒绝访问然后停止运行的情况！\n使用n+Enter取消运行,Enter继续运行')
    Pause = input('按Enter键继续...')
    if Pause != 'n':
        tree(path)

print(user + ' 并不是一个可用的命令。')
continue
continue
