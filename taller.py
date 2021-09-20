# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 19:40:17 2021

@author: Carlos Perez
"""

#Punto 1
# Automoviles check placas 


def checkPlacas(nAutos):
    
    result = {
        'amarillo': 0,
        'rosa': 0,
        'roja': 0,
        'verde': 0,
        'azul': 0        
        }
    
    for i in range(0, nAutos):
        nPlaca = input(f'Digite placa de auto {i+1}: \n')
        lon = len(nPlaca)
        ultNum = int(nPlaca[lon-1])
                      
        if ultNum == 1 or ultNum == 2:
            result['amarillo'] += 1
        elif ultNum == 3 or ultNum == 4:
            result['rosa']  += 1
        elif ultNum == 5 or ultNum == 6:
            result['roja']  += 1
        elif ultNum == 7 or ultNum == 8:
            result['verde']  += 1
        else:
            result['azul']  += 1
            
    return result
    
nAutos = int(input('Digite la cantidad de carros a verificar: \n'))
result = checkPlacas(nAutos)
print(f"La cantidad de autos amarillo es: {result['amarillo']}")
print(f"La cantidad de autos rosa es: {result['rosa']}")
print(f"La cantidad de autos roja es: {result['roja']}")
print(f"La cantidad de autos verde es: {result['verde']}")
print(f"La cantidad de autos azul es: {result['azul']}")

        