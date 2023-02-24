print("-"*12) #question enunciado: cada km rodado, cobra R$0.60, cada dia cobra R$180,00.

print("Car List:\n1 - Ferrari (R$500,00 diária/R$4.20 per km)\n2 - Buggati (R$1000,00 diária/R$6.20 per km)\n3 - Popular Car (R$180,00 diária/R$0.60 per km)")

choice = int(input('\nUr prefeer choice with the name or the number?\nPress 1 - First Option\n      2 - Second Option:\n'))

if(choice == 2):
    car = int(input('Choice ur car number: '))
    km,dia = list(map(float,input('\nType ur km and days count: \n').split()))
    if(car == 1 ):
        print('\nYour car: Ferrari\nYour road {} km, durant {:.0f} days\nIts cost: R${}'.format(km,dia,500.00*dia + km*4.20))

    if(car == 2 ):
        print('\nYour car: Buggati\nYour road {} km, durant {:.0f} days\nIts cost: R${}'.format(km,dia,1000.00*dia + km*6.20))

    if(car == 3 ):
        print('\nYour car: Popular car\nYour road {:.2f} km, durant {:.0f} days\nIts cost: R${}'.format(km,dia,180.00*dia + km*0.60))
        
elif(choice == 1):
    namecar = input("Type the name of car: ")
    km,dia = list(map(float,input('\nType ur km and days count: \n').split()))
    if(namecar == 'Ferrari' ):
        print('\nYour car: Ferrari\nYour road {} km, durant {:.0f} days\nIts cost: R${}'.format(km,dia,500.00*dia + km*4.20))

    if(namecar == 'Buggati' ):
        print('\nYour car: Buggati\nYour road {} km, durant {:.0f} days\nIts cost: R${}'.format(km,dia,1000.00*dia + km*6.20))

    if(namecar == 'Popular car' ):
        print('\nYour car: Popular car\nYour road {:.2f} km, durant {:.0f} days\nIts cost: R${}'.format(km,dia,180.00*dia + km*0.60))
else:
    print('\nWrong Option, try again!')
print("-"*12)