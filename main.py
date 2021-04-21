# Counter():
# Inicializar objetos de contador:

# Formas diferentes de crear contenedores:
print('# Formas diferentes de crear contenedores:')

## Importamos la libreria del reto de Hoy:
from collections import Counter

## Con una secuencia de elementos:
print('## Con una secuencia de elementos:')
print(Counter(['P', 'P', 'P', 'P', 'P', 'P', 'I', 'P', 'E', 'E', 'E' 'I', 'I',]))

## Con Diccionarios:
print('## Con Diccionarios:')
print(Counter({'T': 12, 'E': 9, 'O': 21}))

## Con palabras clave:
print('## Con palabras clave:')
print(Counter(Y=1,A=12,D=21))

# OrderedDict():
print('# OrderedDict():')
from collections import OrderedDict

## Diccionario:
print('Esto es un diccionario: \n')

'Ingresamos el valor de un articulo de la canasta familiar'
print('Ingresamos el valor de un articulo de la canasta familiar')
'Valor en miles de pesos $'

dic = {}
dic['Huevos'] = 12
dic['Arroz'] = 40
dic['Carne'] = 150
dic['Jabón'] = 50


for k,v in dic.items():
  print(k,v)


## En cambio con OrderedDict():
print('## En cambio con OrderedDict():')
'''
copiamos los mismoos articulos pero con
OrderedDict()
'''
ordic = OrderedDict()

ordic['Huevos'] = 12
ordic['Arroz'] = 40
ordic['Carne'] = 150
ordic['Jabón'] = 50

for ok, ov in ordic.items():
  print(ok, ov)

'''
Mientras borra y vuelve a insertar la misma llave,
empujará la llave hasta el final para mantener
el orden de inserción de la llave.
'''
print('\n  Mientras borra y vuelve a insertar la misma llave, empujará la llave hasta el final para mantener el orden de inserción de la llave.')    


print('\n##Antes de eliminar')
for key, value in ordic.items(): 
    print(key, value) 
      
# eliminando un elemento:
ordic.pop('Huevos')
  
# Re-insertando el mismo key => Value:
ordic['Huevos'] = 6.5
  
print('\n##Después de volver a insertar:')
for key, value in ordic.items(): 
    print(key, value)

# DefaultDict():
print('\n# DefaultDict():')
from collections import defaultdict

## Definimos nuestro diccionarios, (int) <= Numeros enteros recibira dic
dic_def = defaultdict(int)

## Definimos una lista  para después iterarla:
from random import randint


lista_num = [randint(i,i+5) for i in range(0,5,1)]

## visualizamos la lista:
print('\n## visualizamos la lista:')

print(lista_num)


## Ahora agregamos los valores al defaultdict:
print('\n## Ahora agregamos los valores al defaultdict:')

for x in lista_num:
  '''
  El valor predeterminado es 0
  así que no hay necesidad de
  ingrese la clave primero
  '''
  dic_def[x] += 1

## Visualicemos nuestro defaultdict:
print('\n## Visualicemos nuestro defaultdict:')
print(dic_def)

## Podemos hacer lo mismo para las listas:
dl = defaultdict(list)

'Definimos un str ya que utlizamos ints anteriormente'

s = 'Reina en mi espíritu una alegría admirable, muy parecida a las dulces alboradas de la primavera, de que gozo aquí'

for z,i in zip(range(len(s.split())),s.split()):
  dl[z].append(i)

print('\nDiccionario con valores como lista.')
print(dl)

# ChainMap():
from collections import ChainMap

## Definimos algunos diccionarios contienen autos con sus respectivas marcas, modelos y años:
print('\n## Definimos algunos diccionarios contienen autos con sus respectivas marcas, modelos y años:')

auto1 = {"marca1": "Ford", "modelo1": "Mustang", "año1": 1964}

auto2 = {"marca2": "Bentley", "modelo2": "Continental GT", "año2": 2003}

auto3 = {"marca3": "Ferrari 458", "modelo3": "458", "año3": 2009}

## encapsulamos todos los diccionarios en una sola unidad:
bd_autos = ChainMap(auto1, auto2, auto3)

print('\n## encapsulamos todos los diccionarios en una sola unidad:')
print(bd_autos)

## Acceder a claves y valores desde ChainMap:

### Acceso a valores usando el nombre de la clave:
print('\n### Acceso a valores usando el nombre de la clave:')
print(bd_autos['marca1'])

### Accediendo a los valores usando values():
print('\n### Accediendo a los valores usando values():')
print(bd_autos.values())

### Accediendo a llaves usando keys():
print('### Accediendo a llaves usando keys():')
print(bd_autos.keys())
