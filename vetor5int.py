#exercicio 1.2 - while/for
vetor = [] # vetor é a variavela que da nome a lista que está vazia e será prenchida com input

for numerosLista in range (5): # o numero limita quantas entradas terá na lista
    numero = int(input("Digite um numero: "))
    vetor.append(numero) # o append serve pra acrescentar os numeros digitdos a lista "vetor"
    
print(vetor)
    
