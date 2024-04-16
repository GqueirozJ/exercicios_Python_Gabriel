print('Calculo de Média')
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
soma = n1 + n2
resultado = soma / 2

print("resultado %.1f" %resultado)
#usei o "%" para formatar 1 número após o ponto

if (resultado >= 6):
  print("Aprovado, Parabéns!!!")
elif (resultado >= 5 or resultado >= 5.9):
  print("Recuperação, melhore!!!")
else: 
  print("Reprovado")
#else não precisa de condição

