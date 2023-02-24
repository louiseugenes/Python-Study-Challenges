import random
print('-'*10)
alunos = input('Digite o nome dos Alunos: ')
lista_alunos = alunos.split()
print('-'*10)
print('Lista dos alunos: ', lista_alunos)
print('-'*10)
n = int(input('Digite quantas equipe serão sorteada: '))

print('\nA ordem de equipe foi: ')
random.shuffle(lista_alunos)
for equipe in range(n):
    print(' {} - {}'.format(n,lista_alunos))

print('-'*10)