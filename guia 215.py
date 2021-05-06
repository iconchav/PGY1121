#Actividad 3

a = int(input("Ingrese numero 1: "))
b = int(input("Ingrese numero 2: "))

if(a<0) or (b<0):
    print("uno de los numeros no es positivo")
else:
    if(a>b):
        print(F"{a} es mayor que {b}")
    elif (a<b):
        print(F"{a} es menor que {b}")
    elif (a==b):
        print(F"{a} es igual que {b}")
