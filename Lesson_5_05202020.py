# file_obj = open('1/123.txt', 'r')
# file = file_obj.read()
# print(file)
# file_obj.close()

# file = open('1/my_file.txt', 'w')
# file.writelines(['1', '2', '3'])
# file.close()


# try:
#     f_obj = open("1/my_file.txt")
#     for line in f_obj:
#         print(line)
# except IOError:
#     print("Произошла ошибка ввода-вывода!")
# finally:
#     f_obj.close()

# with open('1/my_file.txt', 'w') as f:
#     f.write('12')
#     print(f.closed)
#     print(f.mode)
#     print(f.name)

# file_obj = open('1/123.txt', 'w+')
# file_obj.write('qweqwe\nqweqwe\nqweqasd')
# print(file_obj.tell())
#
# file_obj.seek(0)
# print(file_obj.tell())
# print(file_obj.read())
# file_obj.close()

# f = open('123.txt', 'w')
# print('QWE\nqwe\nQWE', file=f)
# f.close()

import os
# os.mkdir('2')
# os.removedirs('2')
# os.remove()
# os.rename()
# print(os.path.basename('path/path2/path3/file.txt'))
# print(os.path.splitext('path/path2/path3/file.txt'))
# print(os.path.join('path/path2/path3/', 'path/path2/path3/file.txt'))

import json

# data = {'income': {'salary': 10, 'bonus': 5}}
# with open('info.json', 'w') as f:
#     json.dump(data, f)

# with open('info.json') as f:
#     data = json.load(f)
#     print(data)

import shutil
shutil.copyfile('123.txt', '234.txt')
shutil.rmtree()
shutil.move()
shutil.copytree()