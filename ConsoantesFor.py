letras = []  # Lista para armazenar as letras
conso = []  # Lista para armazenar as consoantes

print("Digite 10 letras, vamos começar?")
for i in range(10):  # Loop para receber 10 letras
    letra = input(f"Digite a {i + 1}ª letra: ")
    letras.append(letra)  # Adiciona a letra à lista de letras
    if letra.lower() not in ['a', 'e', 'i', 'o', 'u']:  # Verifica se a letra não é uma vogal
        conso.append(letra)  # Adiciona a consoante à lista de consoantes

print(f"As letras digitadas foram: {letras}")
print(f"As consoantes foram: {conso}")
