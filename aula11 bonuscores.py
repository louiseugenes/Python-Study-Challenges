#style 0 - nenhum; 1 - negrito; 4 - sublinhado; 7 - negativo
#text 30 white; 31 red; 32 green; 33 yellow; 34 blue; 35 purple; 36 blue ciano; 37 cinza
# back 40 - 47 (the same ordem do de cima do (text))
# \033[stle;text;backm]  inicia no inicio do print antes do texto e depois das aspas
# \033[m  finaliza o esquemas de cores, coloca no final do print onde quer encerrar
from time import sleep
import random
print('-'*10)
print('Desafio 28\n')

n_a = int(input('Choice ur aleatory number (0 - 5): '))
n_r = random.randint(0,5)
print('\033[1;33m-=-'*10)
print('\033[1;32;40mPROCESSING...\033[m')
print('\033[1;33m-=-'*10)
sleep(3)
print('\033[34;40mYou win!\033[m\n' if n_r == n_a else '\033[31;40mYou loose!\033[m\n')


print('Desafio 29') 
print('\033[1;33m-=-\033[m'*10)
v_c = int(input('\033[0;0;0mType the car velocity: '))
v_l = 80
multa = 0

for i in range(v_l, v_c):
    if v_c > v_l:
        multa += 7
    
if v_c > v_l:
    print('\033[4;31;40mVocê foi multado!\033[m\nSua multa ficará no valor de: \033[31mR${:.0f}.00\033[m'.format(multa))
else:
    print('Você está dirigindo em segurança!')

print('-'*10)
print('Desafio 30\n')

nparimpar = int(input('Choice a number to know if his Par or Impar: '))

print('Par!' if nparimpar%2==0 else 'Impar')

print('-'*10)
print('Desafio 31\n')

km = int(input('Type the KM value to calculate ur travel price: '))
value = 0.0
for i in range(km):
    if km <= 200.00:
        value += 0.50
    else:
        value += 0.45

print('The price of ur travel is: R${:.2f}\n'.format(value))
print('-'*10)
print('Desafio 32\n')

year = int(input('Type a year to know if his are a bissexto: '))
if year%4==0:
    print('Its a bissexto year!')
else:
    print('ARENT a bissexto year! ):')

print('-'*10)
print('Desafio 33\n')

a1,a2,a3 = list(map(int,input('Type 3 numbers (How is the maior and how is the Menor): ').split()))
r = 0
r = a1
if a3 > a1:
    a1 = a3 
if a2 > a1:
    a1 = a2
if a2 < a3:
    a3 = a2
if a1 < a3:
    a3 = a1
if a1 > r:
    a3 = r

print('{} é o maior\n{} é o menor'.format(a1,a3))

print('-'*10)
print('Desafio 34\n')
aumento = 0
salary = float(input('What is ur sallary? '))
if salary > 1250:
    aumento = salary * 0.10
else: 
    aumento = salary * 0.15 
print('Você receberá um aumento de R${:.2f}'.format(aumento))

print('-'*10)
print('Desafio 35\n')

r1,r2,r3 = list(map(int, input('Type 3 retas (Its a triangulo?): ').split()))

if r1 + r2 > r3 and r2 + r3 > r1 and r1 + r3 > r2:
    print('É um triangulo!')
else:
    print('Não é um triangulo ):\n')
print('-'*10)
print('Finish!')
print('-'*10)


