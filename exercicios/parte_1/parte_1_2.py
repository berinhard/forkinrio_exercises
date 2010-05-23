#-*- coding: utf-8 -*-
'''
Implementar uma função que retorne verdadeiro se o número for primo
(falso caso contrário). Testar de 1 a 100.
'''

import string

#função
def eh_primo(num):
    
    # 0 e 1 não são primos
    if num < 2:
        return False

    # 2 é primo
    if num == 2:
        return True

    # qualquer número par não é primo
    if num % 2 == 0:
        return False

    # começamos em um for que começa de 3, vai até num / 2 e vendo somente os ímpares
    for i in range(3, (num / 2) + 1, 2):
        if i <= 1:
            continue
        if num % i == 0:
            return False
    return True

#executável
template = string.Template('$numero é primo? $resultado')
for i in range(1, 101):
    out = template.substitute({'numero' : i,
                               'resultado' : eh_primo(i)})
    print out
