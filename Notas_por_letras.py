print ("Notas por letras")
nota = int (input('Digite a nota de 0 a 100: '))

if (nota == 0):
    print('E')
elif (nota == 1 or nota<36):
    print ('D')
elif (nota == 36 or nota<61):
    print('C')
elif (nota == 61 or nota<86):
    print ('B')
elif (nota == 86 or nota<101):
    print ('A')
else:
    (nota >100)
    print ('Nota inválida')

