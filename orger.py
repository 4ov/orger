#!/usr/bin/python3

import csv
import os
import shutil
import sys
import getpass

username = getpass.getuser()



unsuported = 0

try:
    root_dir = sys.argv[1]
except:
    root_dir = '.'


with open(f'/home/{username}/.filetypes', newline='') as csvfile:
    x = csv.reader(csvfile, delimiter=',', quotechar='|')
    exts = []
    dirs = []
    for r in x:
        if len(r) == 2:
            exts.append(r[0])
            dirs.append(r[1])
        else : 
            pass

for dir in dirs:
    if not os.path.exists(f'{root_dir}/{dir}'):
        os.makedirs(f'{root_dir}/{dir}')




files = os.listdir(root_dir)

for file in files:
    if(not '.' in file):
        pass
    else : 
        ext = file.split('.')[-1]
        if ext in exts :
            index = exts.index(ext)
            shutil.move(f'{root_dir}/{file}', f'{root_dir}/{dirs[index]}/{file}')
        else :
            unsuported += 1



print(f'{unsuported} file(s) not supported')