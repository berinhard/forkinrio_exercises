#-*- coding: utf-8 -*-

'''
2. Implementar um módulo com duas funções:
    ▪ matrix_sum(*matrices), que retorna a matriz soma de matrizes de duas
      dimensões.
    ▪ camel_case(s), que converte nomes para CamelCase.
'''

def matrix_sum(*matrices):
    matrix_a = matrices[0]
    matrix_b = matrices[1]
    matrix_c = []

    #quero um jeito melhor!!!!
    for i in range(2):
        matrix_line = []
        for j in range(2):
            matrix_line.append(matrix_a[i][j] + matrix_b[i][j])
        matrix_c.append(matrix_line)

    return matrix_c

#gostaria de saber se alguém fez com expressão regular...
#senão, como seria?
def camel_case(s):
    #tem outro jeito mais bonito de fazer isso sem expressão regular?
    words_list = s.split(' ')
    word_list = [word[0].upper() + word[1:] for word in words_list]
    camel_case_string = ''.join(word_list)

    return camel_case_string

















