#coding: utf-8

'''
1. Implementar uma classe Animal com os atributos: nome, espécie, gênero,
peso, altura e idade. O objeto derivado desta classe deverá salvar seu estado
em arquivo com um método chamado “salvar” e recarregar o estado em um
método chamado “desfazer”.
'''

import pickle

class Animal(object):

    def __init__(self, nome='', especie='', genero='', peso='', altura='', idade=''):
        self.nome = nome
        self.especie = especie
        self.genero = genero
        self.peso = peso
        self.altura = altura
        self.idade = idade

    def salvar(self):
        serial = {
            'nome':self.nome,
            'especie':self.especie,
            'genero':self.genero,
            'peso':self.peso,
            'altura':self.altura,
            'idade':self.idade,
        }
        nome_arq = '%s.pkl' % self.nome
        pickle.dump(serial, file(nome_arq, 'w'))

    def desfazer(self, nome_do_animal=''):
        if not nome_do_animal:
            nome_do_animal = self.nome
        nome_arq = '%s.pkl' % nome_do_animal
        serial = pickle.load(file(nome_arq))
        print serial
        self.nome = serial['nome']
        self.especie = serial['especie']
        self.genero = serial['genero']
        self.peso = serial['peso']
        self.altura = serial['altura']
        self.idade = serial['idade']
