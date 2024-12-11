def cuadrado(a):
    peri = a + a + a + a
    area = a * a
    print("El perimetro del cuadrado es:",peri)
    print("El area del cuadrado es:",area)

def rectangulo(a,b):
    peri = a + a + b + b
    area = a * b
    print("El perimetro del rectangulo es:",peri)
    print("El area del rectangulo es:",area)

def triangulo(a,b,c):
    h = (b + c) / 2
    peri = a + b + c
    area = (a * h) / 2
    print("El perimetro del triangulo es:",peri)
    print("El area del triangulo es:",area)

def rombo(a):
    d = (a / 4) + a
    c = (a / 4) + a
    peri = a + a + a + a
    area = (d * c) / 2
    print("El perimetro del rombo es:",peri)
    print("El area del rombo es:",area)

def paralelogramo(a,b):
    h = (a + b) / 2
    peri = a + a + b + b
    area = a * h
    print("El perimetro del paralelogramo es:",peri)
    print("El area del paralelogramo es:",area)

def trapecio(a,b,c,d):
    h = (b + c + d) / 3
    peri = a + b + c + d
    area = ((a + b) / 2) * h
    print("El perimetro del trapecio es:",peri)
    print("El area del trapecio es:",area)

def poligono(a):
    apo = (a / 4) * 3
    peri = a * 6
    area = (peri * apo) / 2
    print("El perimetro del poligono regular es:",peri)
    print("El area del poligono regular es:",area)

def circulo(a):
    pi = 3.14
    peri = (2 * pi) * a
    area = pi * (a * a)
    print("El perimetro del circulo es:",peri)
    print("El area del circulo es:",area)