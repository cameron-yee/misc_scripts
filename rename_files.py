import sys
import os
from glob import glob

def inp():
    f = input('File Path: ')
    return f


def renameFile(f):
    b = os.path.basename(f)
    l = b.lower()
    n = l.replace(' ','_') 
    d = os.path.dirname(f)
    sf = str(f)
    sdn = str(d + '/' + n)
    os.rename(sf,sdn)


def getFilePaths(directory):
    files = []
    files.append(glob(directory + '{}'.format('/*.pdf'), recursive=True))
    files = files[0]
    return files


if __name__ == '__main__':
    #f = inp()
    #directory = '/Users/cyee/Desktop/pdf_concat/mnstl_elm_segment_7/lesson_1'
    directory = os.getcwd()
    files = getFilePaths(directory)
    for f in files:
        renameFile(f)
