import string


cadenaADNPrueba =input("Poner la cadena de ADN a Analizar las cadenas promotoras: ") 
solucion = []

while 'TATAAA' in cadenaADNPrueba :   
    restoCadena = cadenaADNPrueba.partition('TATAAA')[2]
    cadenaPromotora=restoCadena.partition('TATAAA')[0]
    solucion.append('TATAAA' + cadenaPromotora + 'TATAAA')
    cadenaADNPrueba= restoCadena.partition('TATAAA')[2]

print('Cadenas promotoras :')
print(solucion)