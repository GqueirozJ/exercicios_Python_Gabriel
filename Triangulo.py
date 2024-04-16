primeirolado = int(input('Digite o tamanho do primeiro lado do triângulo: '))
segundolado = int(input('Digite o tamanho do segundo lado do triângulo: '))
terceirolado = int(input('Digite o tamanho do terceiro lado do triângulo: '))

#Verificando se os Lados formam um triângulo
if primeirolado + segundolado > terceirolado or primeirolado + terceirolado > segundolado or segundolado + terceirolado > primeirolado:
  if primeirolado == segundolado and segundolado == terceirolado:
      print("Os lados formam um triângulo equilátero.")
  elif primeirolado == segundolado or primeirolado == terceirolado or segundolado == terceirolado:
      print("Os lados formam um triângulo isósceles.")
  else:
        print("Os lados formam um triângulo escaleno.")
else:
    print("Os lados não formam um triângulo.")
    
