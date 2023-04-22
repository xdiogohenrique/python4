valor1 = int (input("Insira o primeiro valor:" ))
valor2 = int (input("Insira o segundo valor: " ))

operacao = (input("Qual a operação deseja realizar?"))

if operacao=="+" or operacao=="soma":
  print("O valor da soma é:", valor1+valor2)

elif operacao=="-" or operacao=="subtração":
  print("O valor da subtração é:", valor1-valor2)

elif operacao=="*" or operacao=="multiplicação":
  print("O valor da multiplição é:", valor1*valor2)

elif operacao=="/" or operacao=="divisão":
  print("O valor da divisão é:", valor1/valor2)

else:
  print("Valor ou operação inválida")
