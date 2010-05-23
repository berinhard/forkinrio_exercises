#-*- coding: utf-8 -*-

'''
1. Implementar um programa que receba um nome de arquivo e gere
estatísticas sobre o arquivo (número de caracteres, número de linhas e
número de palavras)
'''
import sys
import os
from param_analyser import sys_argv_analysis


def main():

    sys_argv_analysis()

    file_buffer = open(sys.argv[1])
    
    print 'Analyzing the file: ' + os.path.abspath(sys.argv[1]) + '\n'

    line_counter = 0
    char_counter = 0
    word_counter = 0
    for line in file_buffer:
        line_counter += 1
        char_counter += len(line)
        word_counter += len(line.split(' '))
    
    print 'Number of lines: %d' %line_counter
    print 'Number of chars: %d' %char_counter
    print 'Number of words: %d' %word_counter

    file_buffer.close()

if __name__ == '__main__':
    main()
