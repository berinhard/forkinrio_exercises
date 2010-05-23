#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""

def get_special_paths(dirname):
    special_paths = []
    dir_files_paths = os.listdir(dirname)
    for filename in dir_files_paths:
        regex_result = re.search(r'__(\w+)__', filename)
        if regex_result:
            special_path = os.path.abspath(os.path.join(dirname, filename))
            special_paths.append(special_path)
    return special_paths

def copy_special(files_list, dest):
    if not(os.path.exists(dest)):
        os.mkdir(dest)
    abs_path = os.path.abspath(dest)
    for file_path in files_list:
        filename = os.path.basename(file_path)
        shutil.copy(file_path, os.path.join(abs_path, filename))

def zip_files(files_list, zipname):
    command = 'zip ' + zipname + ' ' + ' '.join(files_list)
    status_output = commands.getstatusoutput(command.strip())
    if status_output[0]:
        sys.stderr.write(output)
        sys.exit(1)

def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print "error: must specify one or more dirs"
        sys.exit(1)

    current_dir = args[-1]

    if todir:
        copy_paths =  get_special_paths(current_dir)
        copy_special(copy_paths, todir)
    if tozip:
        copy_paths =  get_special_paths(current_dir)
        zip_files(copy_paths, tozip)

if __name__ == "__main__":
    main()
