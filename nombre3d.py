import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Paso 1 Crear la figura
fig = plt.figure(figsize=(6,6))

#Paso 2 Crear el plano 3D
plano=fig.add_subplot(111,projection='3d')

#Paso 3 Definimos un punto en el espacio
def graficarA(y,color):
    plano.scatter(0,y,0, c=color, marker='o')
    plano.scatter(0.05,y,0.1, c=color, marker='o')
    plano.scatter(0.1,y,0.2, c=color, marker='o')
    plano.scatter(0.15,y,0.3, c=color, marker='o')
    plano.scatter(0.2,y,0.4, c=color, marker='o')
    plano.scatter(0.25,y,0.5, c=color, marker='o')
    plano.scatter(0.3,y,0.6, c=color, marker='o')
    plano.scatter(0.35,y,0.7, c=color, marker='o')
    plano.scatter(0.4,y,0.8, c=color, marker='o')
    plano.scatter(0.45,y,0.9, c=color, marker='o')
    plano.scatter(0.5,y,1, c=color, marker='o')
    plano.scatter(0.55,y,0.9, c=color, marker='o')
    plano.scatter(0.6,y,0.8, c=color, marker='o')
    plano.scatter(0.65,y,0.7, c=color, marker='o')
    plano.scatter(0.7,y,0.6, c=color, marker='o')
    plano.scatter(0.75,y,0.5, c=color, marker='o')
    plano.scatter(0.8,y,0.4, c=color, marker='o')
    plano.scatter(0.85,y,0.3, c=color, marker='o')
    plano.scatter(0.9,y,0.2, c=color, marker='o')
    plano.scatter(0.95,y,0.1, c=color, marker='o')
    plano.scatter(1,y,0, c=color, marker='o')

    plano.scatter(0.3,y,0.4, c=color, marker='o')
    plano.scatter(0.4,y,0.4, c=color, marker='o')  
    plano.scatter(0.5,y,0.4, c=color, marker='o')
    plano.scatter(0.6,y,0.4, c=color, marker='o')
    plano.scatter(0.7,y,0.4, c=color, marker='o')  
def graficarI(y,color):
    plano.scatter(1.5,y,0, c=color, marker='o')
    plano.scatter(1.6,y,0, c=color, marker='o')
    plano.scatter(1.7,y,0, c=color, marker='o')
    plano.scatter(1.8,y,0, c=color, marker='o')
    plano.scatter(1.9,y,0, c=color, marker='o')
    plano.scatter(2,y,0, c=color, marker='o')
    plano.scatter(2.1,y,0, c=color, marker='o')
    plano.scatter(2.2,y,0, c=color, marker='o')
    plano.scatter(2.3,y,0, c=color, marker='o')

    plano.scatter(1.9,y,0.1, c=color, marker='o')
    plano.scatter(1.9,y,0.2, c=color, marker='o')
    plano.scatter(1.9,y,0.3, c=color, marker='o')
    plano.scatter(1.9,y,0.4, c=color, marker='o')
    plano.scatter(1.9,y,0.5, c=color, marker='o')
    plano.scatter(1.9,y,0.6, c=color, marker='o')
    plano.scatter(1.9,y,0.7, c=color, marker='o')
    plano.scatter(1.9,y,0.8, c=color, marker='o')
    plano.scatter(1.9,y,0.9, c=color, marker='o')
    plano.scatter(1.9,y,1, c=color, marker='o')

    plano.scatter(1.5,y,1, c=color, marker='o')
    plano.scatter(1.6,y,1, c=color, marker='o')
    plano.scatter(1.7,y,1, c=color, marker='o')
    plano.scatter(1.8,y,1, c=color, marker='o')
    plano.scatter(1.9,y,1, c=color, marker='o')
    plano.scatter(2,y,1, c=color, marker='o')
    plano.scatter(2.1,y,1, c=color, marker='o')
    plano.scatter(2.2,y,1, c=color, marker='o')
    plano.scatter(2.3,y,1, c=color, marker='o')
def graficarA2(y,color):
    plano.scatter(2.8,y,0, c=color, marker='o')
    plano.scatter(2.85,y,0.1, c=color, marker='o')
    plano.scatter(2.9,y,0.2, c=color, marker='o')
    plano.scatter(2.95,y,0.3, c=color, marker='o')
    plano.scatter(3,y,0.4, c=color, marker='o')
    plano.scatter(3.05,y,0.5, c=color, marker='o')
    plano.scatter(3.1,y,0.6, c=color, marker='o')
    plano.scatter(3.15,y,0.7, c=color, marker='o')
    plano.scatter(3.2,y,0.8, c=color, marker='o')
    plano.scatter(3.25,y,0.9, c=color, marker='o')
    plano.scatter(3.3,y,1, c=color, marker='o')
    plano.scatter(3.35,y,0.9, c=color, marker='o')
    plano.scatter(3.4,y,0.8, c=color, marker='o')
    plano.scatter(3.45,y,0.7, c=color, marker='o')
    plano.scatter(3.5,y,0.6, c=color, marker='o')
    plano.scatter(3.55,y,0.5, c=color, marker='o')
    plano.scatter(3.6,y,0.4, c=color, marker='o')
    plano.scatter(3.65,y,0.3, c=color, marker='o')
    plano.scatter(3.7,y,0.2, c=color, marker='o')
    plano.scatter(3.75,y,0.1, c=color, marker='o')
    plano.scatter(3.8,y,0, c=color, marker='o')

    plano.scatter(3.1,y,0.4, c=color, marker='o')
    plano.scatter(3.2,y,0.4, c=color, marker='o')  
    plano.scatter(3.3,y,0.4, c=color, marker='o')
    plano.scatter(3.4,y,0.4, c=color, marker='o')
    plano.scatter(3.5,y,0.4, c=color, marker='o')  
def graficarF(y,color):
    plano.scatter(4.2,y,0, c=color, marker='o')
    plano.scatter(4.2,y,0.1, c=color, marker='o')
    plano.scatter(4.2,y,0.2, c=color, marker='o')
    plano.scatter(4.2,y,0.3, c=color, marker='o')
    plano.scatter(4.2,y,0.4, c=color, marker='o')
    plano.scatter(4.2,y,0.5, c=color, marker='o')
    plano.scatter(4.2,y,0.6, c=color, marker='o')
    plano.scatter(4.2,y,0.7, c=color, marker='o')
    plano.scatter(4.2,y,0.8, c=color, marker='o')
    plano.scatter(4.2,y,0.9, c=color, marker='o')
    plano.scatter(4.2,y,1, c=color, marker='o')

    plano.scatter(4.3,y,1, c=color, marker='o')
    plano.scatter(4.4,y,1, c=color, marker='o')
    plano.scatter(4.5,y,1, c=color, marker='o')
    plano.scatter(4.6,y,1, c=color, marker='o')
    plano.scatter(4.7,y,1, c=color, marker='o')
    plano.scatter(4.8,y,1, c=color, marker='o')
    plano.scatter(4.9,y,1, c=color, marker='o')
    plano.scatter(5,y,1, c=color, marker='o')
    plano.scatter(5.1,y,1, c=color, marker='o')

    plano.scatter(4.3,y,0.4, c=color, marker='o')
    plano.scatter(4.4,y,0.4, c=color, marker='o')
    plano.scatter(4.5,y,0.4, c=color, marker='o')
    plano.scatter(4.6,y,0.4, c=color, marker='o')

graficarA(0,'red')   
graficarI(0,'red')
graficarA2(0,'red')
graficarF(0,'red')

graficarA(0.2,'blue')   
graficarI(0.2,'blue')
graficarA2(0.2,'blue')
graficarF(0.2,'blue')


#Paso 4 Mostrar el plano 3D
plano.set_xlim(-1,5)
plano.set_ylim(-1.5,1.5)
plano.set_zlim(-1,1.5)

#Paso 5 Definir los ejes
plano.set_xlabel('Eje X')
plano.set_ylabel('Eje Y')
plano.set_zlabel('Eje Z')

#Paso 6: Definir el titulo
plano.set_title('COD-205')

#Paso 6 Mostrar la imagen
plt.show()