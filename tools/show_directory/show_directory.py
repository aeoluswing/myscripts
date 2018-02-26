#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a simple script for recursive directorires and files index'

__author__ = 'jiangyu'

import os
import os.path

def show_dir(path='.', depth=0, maxdepth=20, ignore_path=[]):
    if not isinstance(depth, int) or not isinstance(maxdepth, int):
        print("arguments depth and maxdepth must be int type.")
        return
    if not os.path.exists(path):
        print("no such file or directory.")
        return
    if depth == 0:
        print("current_path:[" + os.path.abspath(path) + "]")
    for item in os.listdir(path):
        # anything in ignore_path will be ignored
        if item in ignore_path:
            continue
        # limit index maxdepth,anything will be ignored if the depth is longer than maxdepth
        elif (maxdepth-depth) <= 0:
            continue
        else:
            newitem = path +'/'+ item
            if os.path.isdir(newitem):
                print("|    " * depth + "|+++ " + item)
                show_dir(newitem, depth+1, maxdepth, ignore_path)
            else:
                print("|    " * depth + "|--- " + item)

if __name__ == '__main__':
    show_dir()