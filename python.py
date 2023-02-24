print("        Bem-vindo!")
print("---------------------------")
print("Programa de Usuário e Soma!\n")

print("-------------- User Area -------------")
user = input("Digite seu usuário: ")
age = input("Digite sua idade: ")
peso = input("Digite seu peso (Em Kg): ")

print("\n-------------- Calc Area -------------")
x = int(input('Escolha o valor de X: '))
y = int(input("Escolha o valor de Y: "))
z = x + y

print("\n-------------- Result -------------")
print('\nUsuario: {}'.format(user))
print('Idade: {}' .format(age) ,'anos')
print('Peso: {}' .format(peso), 'kg')
print('\nResultado de X + Y: {}' .format(z))

