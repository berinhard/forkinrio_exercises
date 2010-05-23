#-*- coding: utf-8 -*-

'''
4. Implementar um módulo com duas funções:
    ▪ split(fn, n), que quebra o arquivo fn em partes de n bytes e salva com
      nomes sequenciais (se fn = arq.txt, então arq_001.txt, arq_002.txt, ... )
    ▪ join(fn, fnlist) que junte os arquivos da lista fnlist em um arquivo só fn.
'''

from os.path import getsize

def join(fn, fnlist):
    file_out = open(fn, 'w')
    for filename in fnlist:
        file_in = open(filename, 'r')
        for line in file_in:
            file_out.write(line)
        file_in.close()
    file_out.close()

def split(fn, n):
    #depois olhar como criar exceção em python e se é possível para lançar uma
    #isso também surgiu na refatoração e está tarde!!!
    if n > getsize(fn):
        return #exceção?
    file_in = open(fn, 'r')
    file_counter = 0
    #lê n bytes do arquivo e seta o ponteiro de leitura onde ele termina a leitura
    n_bytes_string = file_in.read(n)
    while n_bytes_string != '':
        file_counter += 1
        file_out = open(fn[:-4] + '_%03d.txt' %file_counter, 'w')
        file_out.write(n_bytes_string)
        file_out.close()
        n_bytes_string = file_in.read(n)
    file_in.close()

if __name__ == '__main__':
    join('arq_do_join.txt', ['arq_exerc_01.txt', 'arq_exerc_03.txt'])
    split('arq_grande.txt', 30)
