import string
import random

tablaARNcodificante = {
     'A':['GCU','GCC','GCA','GCG'] , 'D':['GAU','GAC'] , 'E':['GAA','GAG'],
     'R':['CGA','CGC','CCG','CGU','AGA','AGG'] , 'K':['AAG','AAA'] ,'N':['AAC','AAU'],
     'H':['CAC','CAU'] , 'Q':['CAA','CAG'] , 'S':['UCU','UCC','UCA','UCG','AGU','AGC'],
     'T':['ACU','ACC','ACA','ACG'] , 'G':['GGU','GGC','GGA','GGG'] , 'V':['GUA','GUC','GUG','GUU'],
     'P':['CCA','CCC','CCG','CCU'] , 'L':['CUA','CUC','CUG','CUU','UUA','UUG'] , 'F':['UUC','UUU'],
     'Y':['UAC','UAU'] , 'I':['AUA','AUC','AUU'] , 'M':['AUG'] ,
     'W':['UGG'], 'C':['UGC','UGU'] 
 }

cadenaPelpidos = input("Poner la cadena de peptidos: ") 
salidaDelPrograma = ''
while cadenaPelpidos: 
  salidaDelPrograma += random.choice(tablaARNcodificante[cadenaPelpidos[0]])
  cadenaPelpidos = cadenaPelpidos[1:len(cadenaPelpidos)]

print('Cadena ARN codificante valida : ' + salidaDelPrograma)