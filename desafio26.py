name = str(input('Type one frase: ')).upper().strip()
letra = 'A'
print('The letter {} appears {} times in the frase'.format(letra, name.count(letra)))
print('The first letter {} appears in {} position'.format(letra, name.find(letra)+1))
print('The last letter {} appears in {} position'.format(letra, name.rfind(letra)+1))
