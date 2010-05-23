#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import sys
import commands

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it - OK
 -Extract the names and rank numbers and just print them - OK
 -Get the names data into a dict and print it OK
 -Build the [year, 'name rank', ... ] list and print it OK
 -Fix main() to use the extract_names list OK
"""

def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """

    file_buffer = open(filename)
    file_content = file_buffer.read();
    regex_result = re.findall(r'Popularity in (\d\d\d\d)', file_content)
    #search += re.findall(r'<.*?>(\w+)', file_content) --> erro porque pega tudo
                                                    # que esta entre tags
    #search += re.findall(r'<.*?>(\d+)[<.*?>(w+)]', file_content) --> erro porque pega so
                                                    # o numero (por que?)
    regex_result += re.findall(r'<.*?>(\d+)<.*?>(\w+)<.*?>(\w+)', file_content)
    file_buffer.close()

    del file_content
    year = int(regex_result[0])
    name_list = regex_result[1:]
    del regex_result

    print 'Ano: %d' %year
    print '\nLista de tuplas gerada pela leitura: ', name_list

    name_dict = {}
    for tuple_name in name_list:
        name_dict[tuple_name[1]] = name_dict[tuple_name[2]] = int(tuple_name[0])
    print '\nDicionario gerado: ', name_dict

    name_list = []
    name_list.append(year)
    name_list += [name[0] + ' ' + str(name[1]) for name in sorted(name_dict.items())]

    return name_list

def write_result(name_list):

    filename = 'baby' + str(name_list[0]) + '.txt'
    f = open(filename, 'w')
    f.write('Ano: %d' %name_list[0])
    f.write('\n\n=== Lista de nomes ===\n')
    for name in name_list[1:]:
        f.write('\n' + name)
    f.close()
    commands.getoutput('gedit ' + filename)
    

def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
    args = sys.argv[1:]

    if not args:
        print 'usage: [--summaryfile] file [file ...]'
        sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
    summary = False
    if args[0] == '--summaryfile':
        summary = True
        del args[0]

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
    for filename in args:
        name_list = extract_names(filename)
        write_result(name_list)
  
if __name__ == '__main__':
  main()
