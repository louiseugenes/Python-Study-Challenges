n = int(input('Type a number: '))
lrange = int(input('Type a limit of for: '))
for numero in range(lrange):
    print('{} x {} = {}'.format(n,numero+1,n*(numero+1)))

