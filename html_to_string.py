#!/usr/local/bin/python3

import sys

def getFileLines(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        return lines


def concatArrayIntoString(array):
    string = ''

    for item in array:
        if type(item) is str:
            string += item

    return string



if __name__ == '__main__':
    file_path = sys.argv[1]
    lines = getFileLines(file_path)
    string = concatArrayIntoString(lines)
    print(repr(string))

