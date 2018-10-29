#!/usr/local/bin/python3

import pdfkit
import sys
from glob import glob

def globHtml(directory):
    html_files = []
    html_files.append(glob(directory + '{}'.format('/**/*.html'), recursive=True))
    return sorted(html_files[0])

def htmlToPDF(html_files, output_name):
    #1st parameter is list of files, 2nd parameter is output pdf name
    pdfkit.from_file(html_files, '{}.pdf'.format(output_name))


if __name__ == '__main__':
    directory = sys.argv[1]
    html_files = globHtml(directory)
    
    output_name = '/Users/cyee/Documents/3dmss/te_pdfs/{}/{}'.format(sys.argv[2], sys.argv[2])

    htmlToPDF(html_files, output_name)
    
