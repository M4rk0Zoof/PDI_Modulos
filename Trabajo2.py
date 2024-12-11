import matematica.geometria
num = 0
a = 0
b = 0
c = 0
d = 0

print("¡Hola!¿que figura le gustaria calcular?\n1_Cuadrado\n2_Rectangulo\n3_Triangulo\n4_Rombo\n5_Paralelogramo\n6_Trapecio\n7_Poligono\n8_Circulo\n")
num=int(input())
if num == 1:
    print("Ingrese el tamanio de los lados del cuadrado:")
    a=int(input())
    print(matematica.geometria.cuadrado(a))

if num == 2:
    print("Ingrese el tamanio de dos lados del rectangulo y otro para los dos restantes:")
    a=int(input())
    b=int(input())
    print(matematica.geometria.rectangulo(a,b))

if num == 3:
    print("Ingrese el tamanio de los tres lados del triangulo:")
    a=int(input())
    b=int(input())
    c=int(input())
    print(matematica.geometria.triangulo(a,b,c))

if num == 4:
    print("Ingrese el tamanio de los lados del rombo:")
    a=int(input())
    print(matematica.geometria.rombo(a))

if num == 5:
    print("Ingrese el tamanio de dos lados del paralelogramo y otro para los dos restantes:")
    a=int(input())
    b=int(input())
    print(matematica.geometria.paralelogramo(a,b))

if num == 6:
    print("Ingrese el tamanio de cada uno de los lados del trapecio:")
    a=int(input())
    b=int(input())
    c=int(input())
    d=int(input())
    print(matematica.geometria.trapecio(a,b,c,d))

if num == 7:
    print("Ingrese el tamanio de los lados del poligono regular:")
    a=int(input())
    print(matematica.geometria.poligono(a))

if num == 8:
    print("Ingrese el radio del circulo:")
    a=int(input())
    print(matematica.geometria.circulo(a))