#!/usr/local/bin/python3

import sys
from os import listdir
from os.path  import isfile, join

def getFiles(directory):
    files = [f for f in listdir(directory) if isfile(join(directory, f))]
    return files

def alterFiles(directory, files):
    for fi in files:
        with open('{}{}'.format(directory, fi), 'r') as f:
            lines = f.readlines()
            relevant_lines = lines[2] #whatever line range you want to manipulate
            print(lines)

if __name__ == '__main__':
    directory = sys.argv[1]
    files = getFiles(directory)
    alterFiles(directory, files)

