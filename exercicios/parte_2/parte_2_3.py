#-*- coding: utf-8 -*-

'''
3. Implementar uma função que leia um arquivo e retorne uma lista de tuplas
com os dados (o separador de campo do arquivo é vírgula), eliminando as
linhas vazias. Caso ocorra algum problema, imprima uma mensagem de
aviso e encerre o programa.
'''

import sys
import os
from param_analyser import sys_argv_analysis

def analysis_func(file_buffer):
    
    analysis_list = []
    for line in file_buffer:
        if line != '\n' and len(line) != 0:
            new_tuple = ()
            list_format = line.split(',')
            new_tuple = tuple(list_format)
            analysis_list.append(new_tuple)
    return analysis_list

def main():

    sys_argv_analysis()

    try:
        file_buffer = open(sys.argv[1])
        #file_buffer = open(sys.argv[1] + 'da') #para testar o except de bobeira
        analysis_list = analysis_func(file_buffer)
        print analysis_list
    except:
        #como mudei isso na refatoração e são 02:57 da manhã, perguntar como
        #saber qual erro que ocorreu
        print 'Algum erro ocorreu...'
        sys.exit(1)

    file_buffer.close()

if __name__ == '__main__':
    main()
