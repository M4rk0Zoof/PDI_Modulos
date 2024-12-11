import matematica.aritmetica
a = 0
b = 0
c = 0

print("¡Hola!¿que le gustaria hacer?\n1_Sumar\n2_Restar\n3_Multiplicar\n4_Dividir\n")
c=int(input())
if c == 1:
    print("Ingrese los valores de A y B:")
    a=int(input())
    b=int(input())
    print(matematica.aritmetica.sumar(a,b))

if c == 2:
    print("Ingrese los valores de A y B:")
    a=int(input())
    b=int(input())
    print(matematica.aritmetica.restar(a,b))

if c == 3:
    print("Ingrese los valores de A y B:")
    a=int(input())
    b=int(input())
    print(matematica.aritmetica.multiplicar(a,b))

if c == 4:
    print("Ingrese los valores de A y B:")
    a=int(input())
    b=int(input())
    print(matematica.aritmetica.dividir(a,b))