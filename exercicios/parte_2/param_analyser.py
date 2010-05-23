# encoding: utf-8

import sys
import os

def sys_argv_analysis():
    if len(sys.argv) != 2:
        print 'The correct way is: ./' + sys.argv[0] + ' file_path'
        sys.exit(1)
    txt_file_analysis(sys.argv[1])

def txt_file_analysis(file_name):
    if not(os.path.exists(file_name)):
        print 'The file ' + file_name + ' does not exist!'
        sys.exit(1)

    if file_name[-4:] != '.txt':
        print 'The file is not a .txt!'
        sys.exit(1)
