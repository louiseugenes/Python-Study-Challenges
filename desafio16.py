from math import trunc
n = float(input('Type any number: '))
print('The number {} have the part inteira: {}'.format(n,trunc(n)))
#math.trunc é para mostrar a porção inteira do numero '-'

#outra maneira de mostrar essa porção inteira é .format(n,int(n)) (Maneira sem importar biblioteca)