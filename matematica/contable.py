def porcentajes(s):
    print("\nLos porcentajes de descuento son:\nObra social: 2%")
    print("INSSJP: 3%")
    print("Sindicato: 3%")
    print("Jubilacion: 11%")

def descuentos(s):
    jub = (s / 100) * 11
    inss = (s / 100) * 3
    sind = (s / 100) * 3
    obra = (s / 100) * 2
    print("\nLos descuentos en los sueldos son:\nObra social: ",obra)
    print("INSSJP: ",inss)
    print("Sindicato: ",sind)
    print("Jubilacion: ",jub)

def incrementos(s):
    incremento = s * 1.11
    print("Su sueldo podría aumentar un 11%.")
    print("Que vendría siendo:",incremento)

def interes(s):
    interes = s * 0.90
    print("Los intereses podrían restar 10 por ciento del sueldo")
    print("Que vendría siendo:",interes)

def calculoJubilatorio(s):
    caljub = s / 100 * 11
    print("El calculo jubilatorio sería:",caljub)

def calculoObraSocial(s):
    calobra = s / 100 * 2
    print("El calculo de la obra social sería:",calobra)

def calculoSindicato(s):
    calsind = s / 100 * 3
    print("El calculo del sindicato sería:",calsind)

def promedio(s):
    diario = s / 25
    print("El promedio diario del sueldo sería:",diario)

def cuotasinteres(s):
    sininteres = s * 1.13
    print("A la hora de comprar algo, habría 12 por ciento de cuotas sin interes.")
    print("Que sería como si su sueldo fuese:",sininteres)

def cuotaconteres(s):
    coninteres = s * 0.95
    print("A la hora de comprar algo, habría 5 por ciento de cuotas con interes.")
    print("Que sería como si su sueldo fuese:",coninteres)