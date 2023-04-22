from multiprocessing.spawn import import_main_path
import_main_path

a = float(input("Insira o valor de A:"))
b = float(input("Insira o valor de B:"))
c = float(input("Insira o valor de C:"))

delta = b*b-4*a*c

if delta < 0:
    print("Não há raízes reais")
      
elif delta == 0:
    print("Há uma raiz distinta apenas")

else:
    print("Há duas raízes distintas")
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("As raízes são: " x1 "e" x2)
 
else:
    print("Operação inválida")