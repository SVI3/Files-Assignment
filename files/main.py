__winc_id__ = 'ae539110d03e49ea8738fd413ac44ba8'
__human_name__ = 'files'

import os, shutil, zipfile
from os import path
from shutil import copyfile

def clean_cache():
    dir = 'cache'
    if path.exists(dir):
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
    else:
        os.mkdir(dir)
        
def clean_cache_dir(dir):
    if path.exists(dir):
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))
    else:
        os.mkdir(dir)

def cache_zip(zip_file, cache_dir):
    clean_cache_dir(cache_dir)
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(cache_dir)

def cached_files():
    if os.listdir('cache/'):
        path_list = []
        for dirpath,_,filenames in os.walk('cache/'):
            for f in filenames:
                path_list.append(os.path.abspath(os.path.join(dirpath, f)))
        return path_list
    else:
        print('no files in this folder..')

def find_password(path_list):
    for i in path_list:
        file = open(i, 'r')
        contents = file.read()
        search_word = "password"
        file.close()
        if search_word in contents:
            file2 = open(i, 'rt')
            for line in file2:
                if search_word in line:
                    return line[10:-1]
    