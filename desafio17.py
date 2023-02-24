import math
#Tem de ou jeito usando apenas h = math.hypot(Ca,Co), ai é so dar o print .format(h), que ai já mostra a hipotenusa
co,ca = list(map(float, input('Insira o cateto adjacente e o oposto: ').split()))
r = math.pow(ca,2)+math.pow(co,2)
print('O cateto adjacente: {:.0f}\nE o cateto oposto: {:.0f}\nTem a hipotenusa: {:.24f}'.format(ca,co,math.sqrt(r)))