#-*- coding: utf-8 -*-

'''
6. Faça um script que:
    ▪ Leia um arquivo texto.
    ▪ Conte as ocorrências de cada palavra.
    ▪ Mostre os resultados ordenados pelo número de ocorrências
'''

import sys
from param_analyser import sys_argv_analysis

def get_word_count(tuple_struct):
    return tuple_struct[1]

def main():
    sys_argv_analysis()

    file_buffer = open(sys.argv[1])
    dict_words = {}
    for line in file_buffer:
        words_list = line.split(' ')
        for word in words_list:
            # depois avaliar com expressão regular para 'limpar' word de pontos
            # e caracteres que não sejam letras...
            if dict_words.has_key(word.upper()):
                dict_words[word.upper()] += 1
            else:
                dict_words[word.upper()] = 1
    sorted_list = sorted(dict_words.iteritems(), key=get_word_count)
    for word_and_counter in sorted_list:
        print 'Word: ' + word_and_counter[0] + ' --> ' + str(word_and_counter[1])
    
if __name__ == '__main__':
    main()
