'''
4. Implementar um gerador que leia um arquivo e retorne uma lista de tuplas
com os dados (o separador de campo do arquivo e virgula), eliminando as
linhas vazias. Caso ocorra algum problema, imprima uma mensagem de
aviso e encerre o programa.
'''


import sys
import os

def generate_func(file_buffer):
    for line in file_buffer:
        if line.strip():
            new_tuple = ()
            list_format = [elem for elem in line.split(',') if elem.strip()]
            new_tuple = tuple(list_format)
            yield new_tuple

def main():

    try:
        file_buffer = open(sys.argv[1])
        analysis_list = []
        for line in generate_func(file_buffer):
            analysis_list.append(line)
        print analysis_list
    except Exception as e:
        print e.message
        sys.exit(1)

    file_buffer.close()

if __name__ == '__main__':
    main()
