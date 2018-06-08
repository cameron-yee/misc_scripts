import sys
import os
from glob import glob
import string

def inp():
    f = input('File Path: ')
    return f


def stripPunctuation(name):
    x = string.punctuation.replace('_','')
    punct = x.replace('.','')
    table = str.maketrans('', '', punct)
    final_name = name.translate(table)
    return final_name


def renameFile(f):
    base = os.path.basename(f)
    base_lower = base.lower()
    name = base_lower.replace(' ','_') 
    final_name = stripPunctuation(name)
    dirname = os.path.dirname(f)
    sf = str(f)
    sdn = str(dirname + '/' + final_name)
    os.rename(sf,sdn)


def getFilePaths(directory):
    files = []
    files.append(glob(directory + '{}'.format('/*.pdf'), recursive=True))
    files = files[0]
    return files


if __name__ == '__main__':
    #f = inp()
    #directory = '/Users/cyee/Desktop/pdf_concat/mnstl_elm_segment_7/lesson_1'
    n = '1'
    stripPunctuation(n)
    directory = os.getcwd()
    files = getFilePaths(directory)
    for f in files:
        renameFile(f)
