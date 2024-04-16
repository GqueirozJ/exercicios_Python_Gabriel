operation = input('''Qual o tipo de operação?
+ para adição
- para subitração
* para multiplicação
/ para divisão
''')

n1 = int(input('Digite o primeiro numero! : '))
n2 = int(input('Digite o segundo numero! : '))

if operation == '+':
  print('{} + {} = '.format(n1, n2))
  print(n1 + n2)

elif operation == '-':
  print('{} - {} = '.format(n1, n2))
  print(n1 - n2)

elif operation == '*':
  print('{} * {} = '.format(n1, n2))
  print(n1 * n2)

elif operation == '/':
    if n1 == 0 or n2 == 0:# Acrescentei essa condição para que o programa não trave
    # e exiba uma mensagem para o usuario que não é possivel divisões por 0
      print('Não é possivel fazer divisões por 0')
    else:
      print('{} / {} = '.format(n1, n2))
      print(n1 / n2) 
else:
  print('Digite uma operação valida e tente novamente.')

