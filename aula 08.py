#se eu quiser apenas uma função da biblioteca
# eu uso: from NOMEDABIBILIOTECA import NOMEDAFUNÇÃO
# e para usar no codigo, ex: math.sqrt (BIBLIOTECA.FUNÇÃO)
#math.floor (arredonda o numero)
import math  

n = int(input())
r = math.sqrt(n)

print('A raiz quadrada de {} é {}'.format(n,math.floor(r)))