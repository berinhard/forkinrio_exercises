#-*- coding: utf-8 -*-

'''
5. Crie um script que:
    ▪ Compare a lista de arquivos em duas pastas distintas.
    ▪ Mostre os nomes dos arquivos que tem conteúdos diferentes e/ou que
       existem em apenas uma das pastas.
'''

import glob
import difflib

dir_01 = '/home/bernardofontes/Desktop/exercicios/parte_2/pasta_01/'
dir_02 = '/home/bernardofontes/Desktop/exercicios/parte_2/pasta_02/'

#pego todos os arquivos .txt que estejam em dir_01 e dir_02
files_directory_01 = glob.glob(dir_01 + '*.txt')
files_directory_02 = glob.glob(dir_02 + '*.txt')

#depois tentar fazer isso com ER
#preciso SERIAMENTE fazer isso com ER porque achei isso ridículo!

#iterações para pegar somente o nome do arquivo, sem o caminho dele
for i, file_path in enumerate(files_directory_01):
    index = file_path.rfind('/')
    files_directory_01[i] = file_path[index + 1:]
for i, file_path in enumerate(files_directory_02):
    index = file_path.rfind('/')
    files_directory_02[i] = file_path[index + 1:]

#listas de saída
list_diff_content = []
list_single_directory = []
list_equals = []

#instância da classe Differ que será responsável pela comparação
diffInstance = difflib.Differ()

for file_name in files_directory_01:
    #bloco para ver se o arquivo do dir_01 existe no dir_02 atraavés do nome
    try:
        i = files_directory_02.index(file_name)
    except ValueError:
        list_single_directory.append((file_name, dir_01))
        continue

    #como existe um arquivo com o mesmo nome, aqui ele abre para compará-los
    file_01 = open(dir_01 + file_name)
    file_02 = open(dir_02 + files_directory_02[i])
    
    #comparação
    diffList = list(diffInstance.compare(file_01.readlines(), file_02.readlines()))
    for line in diffList:
        #isso do line[0] é por causa do funcionamento do compare
        if line[0] != ' ':
            list_diff_content.append((file_name, dir_01, dir_02))
            break
    else:
        #se o cara não saiu pelo break, significa que os dois arquivos são iguais
        list_equals.append((file_name, dir_01, dir_02))

for file_name in files_directory_02:
    try:
        i = files_directory_01.index(file_name)
    except ValueError:
        list_single_directory.append((file_name, dir_02))
        continue
    
print 'Arquivos únicos por diretório:'
for file_tuple in list_single_directory:
    print 'Arquivo: ' + file_tuple[0] + '\n    Diretório: ' + file_tuple[1]

print '\nArquivos com conteúdos diferentes:'
for file_tuple in list_diff_content:
    print 'Arquivo: ' + file_tuple[0] + '\n    Diretórios: ' + dir_01 + ' e ' + \
                                                            dir_02
print '\nArquivos iguais:'
for file_tuple in list_equals:
    print 'Arquivo: ' + file_tuple[0] + '\n    Diretórios: ' + dir_01 + ' e ' + \
                                                            dir_02







