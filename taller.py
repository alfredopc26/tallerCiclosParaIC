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
#
#
#Punto 2
#Porcentaje animales Zoo

def porcentajeZoo(animal):

    dAnimal = {
        '1': { 'animal': 'elefante', 'cant': 20 },
        '2': { 'animal': 'jirafa', 'cant': 15 },
        '3': { 'animal': 'chimpance', 'cant': 40 }
        }  
    cat = {
        '1': { 'desc': '0 a 1 año', 'cant': 0, 'porc': 0},
        '2': { 'desc': 'de mas de 1 año y menos de 3', 'cant': 0, 'porc': 0 },
        '3': { 'desc': 'de 3 o mas años', 'cant': 0, 'porc': 0 }
        } 


    for i in range(0, dAnimal[animal]['cant']):
        ed = int(input(f"Digite la edad del {dAnimal[animal]['animal']} #{i+1}: \n"))
        if ed <= 1 and ed > 0:
            cat['1']['cant'] += 1
            cat['1']['porc'] = (cat['1']['cant']*100)/dAnimal[animal]['cant']
        elif ed > 1 and ed < 3:
            cat['2']['cant'] += 1
            cat['2']['porc'] = (cat['2']['cant']*100)/dAnimal[animal]['cant']
        else:
            cat['3']['cant'] += 1
            cat['3']['porc'] = (cat['3']['cant']*100)/dAnimal[animal]['cant']
    
    return {
        'animal': dAnimal[animal],
        'categorias': cat
        }

print("Seleccione un animal: ")
print("1. Elefante")
print("2. Jirafa")
print("3. Chimpance")

animal = input('Digite la cantidad de carros a verificar: \n')
result = porcentajeZoo(animal)
print(f"El animal seleccionado es : {result['animal']['animal']}")
print(f"La cantidad de registros tomados son : {result['animal']['cant']}")
print(f"El porcentaje en la categoria {result['categorias']['1']['desc']} es: ")
print(f"% {result['categorias']['1']['porc']}")
print(f"El porcentaje en la categoria {result['categorias']['2']['desc']} es: ")
print(f"% {result['categorias']['2']['porc']}")
print(f"El porcentaje en la categoria {result['categorias']['3']['desc']} es: ")
print(f"% {result['categorias']['3']['porc']}")
#
#
# Punto 3
# calcular salario obreros

def calcularSalario(numObreros):
    
    for i in range(0, numObreros):
        dias = int(input(f"Cuantos dias trabajo el obrero #{i+1}: \n"))
        if dias <= 40:
            salario = dias * 20
        else:
            salarioBase = dias * 20
            extra = dias - 40
            if extra > 0:
                extraBase = extra * 25
            salario = salarioBase + extraBase
        print(f"El salario del obrero # {i+1} es:")
        print(f"{salario}")
        
obreros = int(input('Digite la cantidad de obreros a evaluar: \n'))
calcularSalario(obreros)
