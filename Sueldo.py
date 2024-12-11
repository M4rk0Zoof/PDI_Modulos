import matematica.contable

a = 0
s = 0

print("¡Hola!¿cual es el sueldo mensual que usted cobra?")
s=int(input())
print("\n¿que le gustaria hacer con su sueldo?\n")
print("1_Porcentajes\n2_Descuentos\n3_Incrementos\n4_Interes simple")
print("5_Calculo del aporte jubilatorio\n6_Calculo del aporte a la obra social\n7_Calculo del aporte al sindicato\n8_Promedio")
print("9_Valor en 12 cuotas sin interes\n10_Valor en 12 cuotas con interes prefijado.\n")

a=int(input())
if a == 1:
    print(matematica.contable.porcentajes(s))

if a == 2:
    print(matematica.contable.descuentos(s))

if a == 3:
    print(matematica.contable.incrementos(s))

if a == 4:
    print(matematica.contable.interes(s))

if a == 5:
    print(matematica.contable.calculoJubilatorio(s))

if a == 6:
    print(matematica.contable.calculoObraSocial(s))

if a == 7:
    print(matematica.contable.calculoSindicato(s))

if a == 8:
    print(matematica.contable.promedio(s))

if a == 9:
    print(matematica.contable.cuotasinteres(s))

if a == 10:
    print(matematica.contable.cuotaconteres(s))