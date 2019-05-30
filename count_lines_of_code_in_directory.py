#!/usr/local/bin/python3
from glob import glob
import sys
import os

def getFilePaths(directory, file_extension):
    files = glob('{}*.{}'.format(directory, file_extension))
    return files


def getFilePathsRecursive(directory, file_extension):
    files = glob('{}**/*.{}'.format(directory, file_extension), recursive=True)
    return files


def countLines(files):
    lines = []

    for fil in files:
        with open(fil, 'r') as f:
            file_lines = f.readlines()
            lines.extend(file_lines)

    print('{} lines'.format(len(lines)))


if __name__ == '__main__':
    directory = sys.argv[1] 
    file_extension = sys.argv[2]

    recursive = sys.argv[3] if len(sys.argv) == 4 else True

    files = None
    if recursive != 'False':
        files = getFilePathsRecursive(directory, file_extension)
    else:
        files = getFilePaths(directory, file_extension)

    countLines(files)
