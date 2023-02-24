print('-'*10)
frase = str(input('Digite a frase: '))
#luis #robenilson
print("\nLargura da frase: {} caracteres".format(len(frase)))
print('-'*10)
letra = str(input('\nEscolha a letra para fazer a contagem: '))
print('Contador de caracteres da letra: -> {} <-\nTotal: {} caracteres'.format(letra,frase.count(letra))) #frase.count(letra,0,13)
print('-'*10)
pfrase = str(input('Escolha alguma parte da frase para indicar a posição dos char.\nWrite: ')) # conta do char 0 até o 13 quantas letra tem

print('\nParte da frase: {}\nPosição: {}'.format(pfrase,frase.find(pfrase)))
print('-'*10)

choice1 = int(input('Escolha:\n1 - Para Fazer Alteração/Substuição na frase\n2 - Para não fazer\nChoice: '))
if choice1 == 1:
    sfrase0, sfrase1 = list(map(str, input('\nEscolha uma palavra que quer substitur e logo em seguida pela qual quer substituir: ').split()))
    print('Sua frase após a substiuição ficou assim:\n{}'.format(frase.replace(sfrase0,sfrase1)))
    frasee = frase.replace(sfrase0,sfrase1)
if (choice1 == 2) or (choice1 == 1):
    print('-'*10)
    choice2 = int(input('\nEscolha:\n1 - Para deixar a frase maiuscula\n2 - Para deixar Minúscula\n3- Para não alterar nada\nChoice: '))
    if choice1 == 2:
        frasee = frase
    if choice2 == 1:
        print('{}'.format(frasee.upper()))
    elif choice2 == 2:
        print('{}'.format(frasee.lower()))
else:
    print('Sua frase ficou assim: ', frasee)
print('-'*10)
choice3 = int(input('Capitalizar a primeira letra da sua frase?\n1 - Sim\n2 - Não\nChoice: '))
if choice3 == 1:
    print('Frase capitalizada: {}'.format(frasee.capitalize()))
if choice3 == 1 or choice3 == 2:
    choice4 = int(input('Deixar cada plavra da frase maiuscula?\n1 - Sim\n2 - Não\nChoice: '))
    if choice4 == 1:
        print('Ficou assim: {}'.format(frasee.title()))
    else:
        print('Sua frase final está assim:\n{}'.format(frasee))

print('-'*10)
print('-'*10)
#parte 2 do estudo

print('\n------- Parte 2 do Estudo ------')

r_space = (int(input('Remover todos os espaços desnecessário da frase?\n1 - Sim!\n2 - Não!\nEscolha: ')))
if r_space == 1 and choice1 == 2:
    print(frase.strip()) #rstrip trica espaço da direita e lstrip da esquerda                   
                            #e strip remove todos os denecessários
elif r_space == 1 and choice1 == 1:
    print(frasee.strip())
elif r_space == 2 and choice1 == 1: 
    print('Sua frase final agora é: {}'.format(frasee))
else:
    print('Sua frase final agora é: {}'.format(frase))

print('-'*10)
print('-'*10)
div_frase = int(input('\nDividir frase em palvras individuais?\n1 - Sim\n2 - Não\nChoice: '))
#exemplo: "Curso em Video", irá ter 3 indices "Curso" "em" "Video", caso queira dividi-los
if div_frase == 1 and choice1 == 1:
    print(frasee.split())
elif div_frase == 1 and choice1 == 2:
    print(frase.split())
elif div_frase == 2 and choice1 == 1:
    print('Como está sua frase: ',frasee)
else:
    print('Como está sua frase: ',frase)
    
print('-'*10)
print('-'*10)
juntar_frase = int(input('\nJuntar frase novamente?\n1 - Sim\n2 - Não\nType: '))
if juntar_frase == 1 and choice1 == 1:
    ''.join(frasee)
    print('Sua frase final é: ',frasee)
elif juntar_frase == 1 and choice1 == 2:
    ''.join(frase)
    print(frase)
elif(juntar_frase == 2 and choice1 == 1):
    print('Sua frase final é: ',frasee)
else:
    print('Sua frase final é: ',frase)
print('-'*10)
print('-'*10)

