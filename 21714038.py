import sys
import math
import random
from builtins import str

correo = "DanielSabbagh@uem.es"
nExpediente = 21714038


def ejA1(n): #Complejidad O(n^3)
    sum = 0
    for i in range (0, n):
        for j in range (0, n*n):
            sum += 1 

def ejA2(n): #Complejidad O(n^4)
    sum = 0
    for i in range (0, n):
        for j in range (0, i*i):
            for k in range (0, j):
                sum +=1

def ejA3(n): #Complejidad O(n/2)
    i = 1
    x = 0
    while (i <= n):
        x += 1
        i += 2

def ejB():
    p = 1 
    if nExpediente < 1: 
        p = 0
    elif nExpediente == 2:
        p = 1
    else: 
        for i in range(2, nExpediente):  
            if nExpediente % i == 0:
                primo = 0
        primo = 1
    if primo == 1:
        print("Tu numero de nExpediente es primo")
    else:
        print("Tu numero de nExpediente no es primo")

    menu(nExpediente) 

def ejC():     
    print("Ingresa el orden de su Matriz 1")
    filas1,columnas1 = int(input()),int(input())
    print("Ingresa el orden de su Matriz 2")
    filas2,columnas2 = int(input()),int(input())

    if (columnas1==filas2):

        matriz1 = []
        for i in range(filas1):
            matriz1.append( [0] * columnas1 )

        matriz2 = []
        for i in range(filas2):
            matriz2.append( [0] * columnas2 )

        print ("Rellene la primera Matriz")
        for i in range(filas1):
            for j in range(columnas1):
                matriz1[i][j] = float(raw_input('Elemento (%d,%d): ' % (i, j)))
        print ("Rellene la segunda Matriz")
        for i in range(filas2):
            for j in range(columnas2):
                matriz2[i][j] = float(raw_input('Elemento (%d,%d): ' % (i, j)))

        matriz3 = []
        for i in range(filas1):
            matriz3.append( [0] * columnas2 )

        for i in range(filas1):
            for j in range(columnas2):
                for k in range(filas2):
                    matriz3[i][j] += matriz1[i][k] * matriz2[k][j]
        print ("Su matriz resultante es")
        print(matriz3)
    else:
        print ("La multiplicacion entre matrices debe ser mxn * nxp")
    menu(nExpediente)

def ejD():
    n = str(nExpediente)
    lista = list(n)
    listaReverse=[lista[i-1] for i in range(len(lista),0,-1)]
     
    if lista == listaReverse:
        print("Tu numero de expediente es Capicua")
    else:
        print("Tu numero de expediente no es Capicua")
    menu(nExpediente)   

def ejE():
    filas = int(input ("Introduzca el numero de filas de sus matrices: "))
    columnas = int(input ("Introduzca el numero de columnas de sus matrices: "))

    matriz1 = []
    matriz2 = []
    matriz3 = []
    for i in range (filas):
        matriz1.append( [0] * columnas)
        matriz2.append( [0] * columnas)
        matriz3.append( [0] * columnas)

    print ("Ingrese su Matriz 1")
    for i in range(filas):
            for j in range(columnas):
                matriz1[i][j] = float(raw_input('Elemento (%d,%d): ' % (i, j)))
    print ("Ingrese su Matriz 2")
    for i in range(filas):
        for j in range(columnas):
                matriz2[i][j] = float(raw_input('Elemento (%d,%d): ' % (i, j)))

    for i in range(filas):
        for j in range(columnas):
                matriz3[i][j] += matriz1[i][j] + matriz2[i][j]
    print ("Su matriz resultante es")
    print (matriz3)
    menu(nExpediente)

def ejF(array):
    c = len(array)
    for i in range(c):
        for j in range(len(array[i])):
            for k in range (len(array[i])-j-1):
                if(array[i][k] > array[i][k+1]):
                    t = array[i][k]
                    array[i][k] = array[i][k+1]
                    array[i][k+1] = t
    print(array)
    menu(nExpediente)


def ejGIterativo(num):
    for i in range(1,num+1):
        if(i== 1 or i==0): 
            fact = 1
        else:
            fact = fact*i
    print('El factorial de ' + str(num) + ' es ' + str(fact) ) 
    menu(nExpediente)
    
def ejGRecursivo(num):
    if num == 0:
        return 1
    else:
        return num *ejGRecursivo(num-1)
    menu(nExpediente)


def login():
    email = input("Ingrese su email de la uem:")
    psw = (input("Ingrese la contrasenia:"))
    contraseniaExpediente = int(psw)
    if(contraseniaExpediente != nExpediente or email != correo):
        print("No autorizado\nSALIENDO DEL PROGRAMA...")
    else: menu(contraseniaExpediente)

def menu(nExpediente):
    print("\n******************** UNIVERSIDAD EUROPEA DE MADRID *************************\n"
         +  "Escuela de Ingenieria Arquitectura y Disenio\n\n")
    print("DANIEL SABBAGH PASTOR - 21714038\n")

    print("*****************MENU**********************\n"
          "B: Ejercicio B\n"
          "C: Ejercicio C\n"
          "D: Ejercicio D\n"
          "E: Ejercicio E\n"
          "F: Ejercicio F\n"
          "G: Ejercicio G\n"
          "S: Salir\n")
    opcion = input("Elija una opcion:")
    
    if opcion == "B" or opcion == 'b':
        ejB()
    elif opcion == "C" or opcion == 'c':
        ejC()
    elif opcion == "D" or opcion == 'd':
        ejD()
    elif opcion == "E" or opcion == 'e':
        ejE()
    elif opcion == "F" or opcion == 'f':
        array = [[21, 71, 40, 38, 21],[9,2,3,4,8]]
        print ("El arrayay ordenado es:")
        ejF(array)
    elif opcion == "G" or opcion == 'g':
        num = 8 
        print("Introduzca 1 para la Forma recursiva")
        print("Introduzca 2 para la Forma iterativa")
        n = int(input("Opcion: "))
        if n == 1:
            print(ejGRecursivo(num))
        elif n ==2:
            ejGIterativo(num)
        else:
            print("No ha introducido un valor correcto")
    else:
        print("Programa Finalizado...")
        exit

login()


