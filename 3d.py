import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Paso 1 Crear la figura
fig = plt.figure(figsize=(6,6))

#Paso 2 Crear el plano 3D
plano=fig.add_subplot(111,projection='3d')

#Paso 3 Definimos un punto en el espacio
plano.scatter(4,5,6, c='g', marker='o')
plano.scatter(6,5,6, c='r', marker='o')
plano.scatter(4,7,6, c='b', marker='o')
plano.scatter(6,7,6, c='y', marker='o')

plano.scatter(4,5,8, c='g', marker='o')
plano.scatter(6,5,8, c='r', marker='o')
plano.scatter(4,7,8, c='b', marker='o')
plano.scatter(6,7,8, c='y', marker='o')


#Paso 4 Mostrar el plano 3D
plano.set_xlim(0,10)
plano.set_ylim(0,10)
plano.set_zlim(0,10)

#Paso 5 Definir los ejes
plano.set_xlabel('Eje X')
plano.set_ylabel('Eje Y')
plano.set_zlabel('Eje Z')

#Paso 6: Definir el titulo
plano.set_title('COD-205')

#Paso 6 Mostrar la imagen
plt.show()