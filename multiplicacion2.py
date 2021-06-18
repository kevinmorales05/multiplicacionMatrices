import numpy as np
from numpy import random as rd


print('Programa para multiplicar Matrices')
print('Matriz A')
a = int(input('Filas: '))
b = int(input('Columnas: '))
dimensionesA = (a,b)
print('Matriz B')
c = int(input('Filas: '))
d = int(input('Columnas: '))
dimensionesB = (c,d)

A =  np.random.random((a,b))*100
B =  np.random.random((c,d))*100
print('Matriz A: ' + str(A))
print('Matriz B: ' + str(B))

print('Resultado de la multiplicación de las Matrices')
arr=np.dot(A, B)
print(arr)