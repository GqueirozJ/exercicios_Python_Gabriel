#exercicio 2.2 - while/for
vetor = [] # vetor é a variavel que da nome a lista que está vazia e será prenchida com input

for numerosLista in range (10): # o numero limita quantas entradas terá na lista
    numero = int(input("Digite um numero: "))
    vetor.append(numero) # o append serve pra acrescentar os numeros digitdos a lista "vetor"
    
vetor.reverse() #como o nome ja diz, ele faz a ordem inversa dos numeros digitados
print(vetor)

