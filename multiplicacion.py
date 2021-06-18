import numpy as np
#algoritmo para crear matrices n dimensionales y tambien para multiplicar matrices

print('Definir dimensiones de las matrices')
print('Matriz A')
matrizAFilas = int(input('Escriba la Cantidad de Filas de Matriz A: '))
matrizAColumnas = int(input('Escriba la Cantidad de Columnas de Matriz A: '))
matrizBFilas = int(input('Escriba la Cantidad de Filas de Matriz B: '))
matrizBColumnas = int(input('Escriba la Cantidad de Columnas de Matriz B: '))
#Matriz A
print('INGRESO DE VALORES DE MATRIZ A')
i = 0
j = 0
MatrizA = []
MatrizB = []
for i in range(0, matrizAFilas):
    print('Fila '+ str(i+1))
    for j in range(0, matrizAColumnas):
        valor = int(input('Ingrese un valor: '))
        MatrizA.append(valor)
        j=j+1
        print(MatrizA)
    i=i+1
    MatrizB.append(MatrizA)
    MatrizA.clear()
   
print('Esta es la matriz A')
print(MatrizB)

#Matriz D

print('INGRESO DE VALORES DE MATRIZ B')
k = 0
l = 0
MatrizC = []
MatrizD = []
for k in range(0, matrizBFilas):
    print('Fila '+ str(k+1))
    
    for l in range(0, matrizBColumnas):
        valor = int(input('Ingrese un valor: '))
        MatrizC.append(valor)
        l=l+1
    k=k+1
    MatrizD.append(MatrizC)
print('Esta es la matriz B')
print(MatrizD)

#Multiplicacion de las matrices

A = np.array(MatrizB) 
B = np.array(MatrizD)
C = np.dot(A,B)
print('*****************************************************************')
print('*****************************************************************')
print('El resultado de la multiplicaciön de matrices es: ')
print(C)