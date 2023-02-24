from fractions import Fraction
aa = input('Type where is ur angle\nB or C: ')
b,c,h = list(map(int, input('Type the medidas\n(A,B,C): ').split()))

if aa == 'B':
    sen = Fraction(c,h)
    cos = Fraction(b,h)
    tang = Fraction(c,b)
    print('\nTangente: {}\nSeno: {}\nCosseno: {}.'.format(tang,sen,cos))

elif aa == 'C':
    sen = Fraction(b,h)
    cos = Fraction(c,h)
    tang = Fraction(b,c)
    print('\nTangente: {}\nSeno: {}\nCosseno: {}.'.format(tang,sen,cos))

# tem como fazer em radianos, ao em vez de fração
# tem que converter  em radiano primeiro, mas posso fazer isso dentro da função
# que ja descobre o sen, cos, e tangente: ficaria assim:
# angulo = float(input())
# seno = math.sin(math.radians(angulo)) e assim sucessivamente ai só da o print
# .format(seno,tan,cos)


