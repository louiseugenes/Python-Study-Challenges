import random
print('-'*10)
alunos = input('Digite o nome dos Alunos: ')
lista_alunos = alunos.split()
print('-'*10)
print('Lista dos alunos: ', lista_alunos)
print('-'*10)
print('O aluno escolhido foi: {}'.format(random.choice(lista_alunos)))
print('-'*10)