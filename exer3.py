produto = input("Insira o nome do produto: ")
valor   = float(input("Insira o valor da compra: "))

if valor < 10.00:
  print("O produto é", produto, ", E o valor da venda é:", valor*0.70)
elif valor < 30.00:
  print("O produto é", produto, " ,E o valor da venda é:", valor*0.50)
elif valor < 50.00:
  print("O produto é", produto, " ,E o valor da venda é:", valor*0.40)
elif valor > 50.00:
  print("O produto é", produto, " ,E o valor da venda é:", valor*0.30)
else: 
  print("O produto/valor estão errados")