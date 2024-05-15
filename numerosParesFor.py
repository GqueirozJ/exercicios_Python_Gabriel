numeros = [] # Lista para armazenar os números
numerosP = [] # Lista para armazenar os números pares
numerosI = [] # Lista para armazenar os números ímpares

print("Digite 10 números inteiros, vamos começar?")
for i in range(10): # Loop para receber 20 números inteiros
    numero = int(input(f"Digite o {i + 1}° número: "))
    numeros.append(numero) # Adiciona o número à lista de números
    if numero % 2 == 0: # Verifica se o número é par
        numerosP.append(numero) # Adiciona o número par à lista de números pares
    else:
        numerosI.append(numero) # Adiciona o número ímpar à lista de números ímpares

print(f"Os números digitados foram: {numeros}")
print(f"Os números pares foram: {numerosP}")
print(f"Os números ímpares foram: {numerosI}")
