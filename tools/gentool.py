# encoding: shift-jis
# -*- coding: utf-8 -*-

import os
import sys
import argparse
import glob
from os import walk


def get_relative_path(home, path):
    x = os.path.relpath(home, path)
    a=len(home)
    b=len(path)
    xx = x[a:b]
    xxx = xx.replace("\\", "/")

    #print('len home = {}, len_x={}'.format(len(home), len(path)))
    #print('####{}->{}->x={}->xx={}'.format(home, path, x,xx))
    if len(xxx) == 0:
        xxx = '.'
    return xxx;


def replace(home, sOilBegin, sOilEnd, sHeaderFile, sFile):
    OIL_HOME = 'UNIQUE_OIL_HOME'
    str_log = ''
    with open(sHeaderFile, 'r') as fh:
        sheader = fh.readlines()
        with open(sFile, 'r') as f:
            str_log += ('reading : {}  +  {}'.format(sFile, sHeaderFile)) + ' ===> '
            ibegin = -1
            iend = -1
            lines = f.readlines()
            for i, s in enumerate(lines):
                if s.find(sOilBegin) != -1:
                    ibegin = i
                elif s.find(sOilEnd)!= -1:
                    iend = i
            if ibegin < iend and ibegin >= 0:
                #sFile += '.t'
                with open(sFile, 'w') as ff:
                    str_log += ('process : {}'.format(sFile))
                    for i, s in enumerate(lines):
                        if i <= ibegin or i >= iend:
                            ff.write(s)
                        if i == iend-1:
                            ff.write("\n<!-- ###################Begin, Do Not Edit, Generate By Tools################### -->\n")
                            for m, sh in enumerate(sheader):
                                relative_dir = get_relative_path(home, sFile)
                                #sh = sh.rstrip(' ')
                                #sh = sh.rstrip('\n')
                                while True:
                                    idx = sh.find(OIL_HOME)
                                    if idx >= 0:
                                        #print('relative path:{}\n'.format(relative_dir))
                                        tsh = sh[0:idx] + relative_dir + sh[idx + len(OIL_HOME):-1]
                                        #print(idx)
                                        sh = tsh
                                        #print(sh)
                                    else:
                                        break
                                #sh += '\n'
                                #print(sh)
                                ff.write(sh)
                            ff.write("\n<!-- ###################End, Do Not Edit, Generate By Tools################### -->\n")
    print(str_log)



def main(arg):

    pass

def select_files(root, files):
    """
    simple logic here to filter out interesting files
    .py files in this example
    """
    selected_files = []

    for file in files:
        #do concatenation here to get full path
        full_path = join(root, file)
        ext = splitext(file)[1]

        if ext == ".html":
            selected_files.append(full_path)

def build_recursive_dir_tree(path):
    path = path.rstrip()
    all = []
    for root, subdirs, files in os.walk(path):
        root = root.rstrip()
        for file in os.listdir(root):
            if (root[len(root)-1] == '\t'):
                root = root[0:len(root)-1]
            if (root[len(root)-1] == '/t'):
                root = root[0:len(root)-1]

            filePath = root + '/' +file
            if os.path.isdir(filePath):
                s = build_recursive_dir_tree(filePath)
                for ss in s:
                    all.append(ss)
            else:
                all.append(filePath)
    return all

def main():
    headerJp = ['<!-- BeginOilHeaderJp -->', '<!-- EndOilHeaderJp -->', '../header_foot_template/headerJp.html']
    footJp = ['<!-- BeginOilFootJp -->', '<!-- EndOilFootJp -->', '../header_foot_template/footJp.html']
    headerEng = ['<!-- BeginOilHeaderEng -->', '<!-- EndOilHeaderEng -->', '../header_foot_template/headerEng.html']
    footEng = ['<!-- BeginOilFootEng -->', '<!-- EndOilFootEng -->', '../header_foot_template/FootEng.html']


    datas = (headerJp, footJp, headerEng, footEng)
    #datas = (headerEng, footEng)

    home = "../"
    paths = build_recursive_dir_tree(home)

    for header_foot in datas:
        for html in paths:
            if html.endswith('.html') == False:
                continue
            #print(html)
            sOilBegin = header_foot[0]
            sOilEnd = header_foot[1]
            sHeaderFile = header_foot[2]
            sFile = html

            if (sHeaderFile != html):
                replace(home, sOilBegin, sOilEnd, sHeaderFile, sFile)

if __name__ == '__main__':
    main()
