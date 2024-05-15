# Exercicio while 3.2
notas = [] # notas é a variavel que da nome a lista que está vazia e será prenchida com input

for i in range(4): # o numero limita quantas entradas terá na lista
    nota = float(input(f"Digite a {i + 1}° nota: "))
    notas.append(nota)

# Mostrar as notas
print("Suas notas são:")
for i, nota in enumerate(notas): #essa função "enumerate" serve pra acessar o que foi inserido
                                 #e a sua posição na lista
    print(f" {i + 1}° Nota: {nota}")

# Calcular a média
soma = sum(notas) #A função "sum" vai somar todos os valores da lista
media = soma / len(notas)#A função "len" está retornando quantos itens tem na lista, por isso aqui
                        #ele esta servindo como multiplicador
                        
print(f"A sua medía foi: {media:.1f}")
