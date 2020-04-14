
# Diccionario Promedio Alumno

materias = {'español':2.3, 'economia':3.2, 'ingles':4.5, 'matematicas':3.7}
notas = sum(materias.values())
promedio = notas / 4
print('El promedio del alumno es de: ' + str(promedio))

# # Lista 10 numeros positivos

print('Ingrese 10 numeros')
num1 = int(input('Numero 1:\n'))
num2 = int(input('Numero 2:\n'))
num3 = int(input('Numero 3:\n'))
num4 = int(input('Numero 4:\n'))
num5 = int(input('Numero 5:\n'))
num6 = int(input('Numero 6:\n'))
num7 = int(input('Numero 7:\n'))
num8 = int(input('Numero 8:\n'))
num9 = int(input('Numero 9:\n'))
num10 = int(input('Numero 10:\n'))

lista = [num1, num2, num3, num4, num5, num6, num7, num8, num9, num10]
print(lista)
suma = 0
for numero in lista:
	suma += numero
print('El total de la lista es: '+ str(suma))
promedio = suma / len(lista)
print('El promedio de la lista de los numeros ingresados es: '+ str(promedio))
numMayor = max(lista)
print('El numero mayor de la lista es:'+ str(numMayor))
numMenor = min(lista)
print('El numero menor de la lista es:'+ str(numMenor))

# Frases que sean Palindromo

print('Ingrese una frase')
frase1 = input('Frase 1:\n')
frase2 = input('Frase 2:\n')
frase3 = input('Frase 3:\n')
frase4 = input('Frase 4:\n')

frases = [frase1, frase2, frase3, frase4]
print(frases)
# #Frecuencia de las palabras
# cadenaPalabras = str(input("Escriba su parrafo a leer: "))
# listaPalabras = cadenaPalabras.split()

# frecuenciaPalab = []
# for w in listaPalabras:
#     frecuenciaPalab.append(listaPalabras.count(w))

# print("Frecuencia de las palabras\n" + str(list(zip(listaPalabras, frecuenciaPalab))))

#Contar vocales
# cad = str(input("Escriba la palabra con vocales: "))
# voc = 0
# for c in cad:
#     if c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c =='O' or c == 'U':
#         voc=voc+1
# print ("Numero de vocales: "+ str(voc))

#Frecuencia de vocales de una frase
# frecuenciaPalab = []
# voc = 0

# cad = str(input("Escriba el parrafo con vocales: "))
# listaPalabras = cad.split()

# for c in listaPalabras:
    
#     if c == 'a' or c == 'e' or c == 'i' or c =='o' or c == 'u' or c == 'A' or c == 'E' or c == 'I' or c =='O' or c == 'U':
#         voc=voc+1
#         frecuenciaPalab.append(listaPalabras.count(c))

# print ("Numero de vocales: "+ str(voc))
# print("Frecuencia de las vocales\n" + str(list(zip(listaPalabras, frecuenciaPalab))))

#Eliminar vocales de palabra
# vocales = ['a','A','e','E','i','I','o','O','u','U']
# res = ''

# cad = str(input("Escriba la palabra con vocales: "))
# for letra in cad:
#     if letra not in vocales:
#         res += letra
# print ("Su palabra sin vocales es: "+ str(res))

#Pares
# par = []

# for i in range(0,100):
#     if (i % 2 == 0):
#         par.append(i)

# print("Los números pares son : " + str(par))