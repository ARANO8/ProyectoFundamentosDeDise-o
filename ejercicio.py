import matplotlib.pyplot as plt

# Para ingresar los puntos del cuadrado por teclado descomentar las siguientes lineas:
# A=[int(input()),int(input())]
# B=[int(input()),int(input())]
# C=[int(input()),int(input())]
# D=[int(input()),int(input())]

# Puntos del cuadrado , para la demostracion empezaremos con las listas ya llenadas
A=[1,3]
B=[3,3]
C=[1,1]
D=[3,1]
# Obtenemos nuestro punto de referencia para la ampliacion , en este caso el punto C
c1=C[0]
c2=C[1]
#Almacenamos en una lista el cuadrado original llamado coordenadas y en otra lista almacenamo la lista con la ampliacion del cuadrado
coordenadas=[A,B,D]
coordenadas2=[A,C,D,B,A]
x=[i[0] for i in coordenadas2]
y=[i[1] for i in coordenadas2]

# Ingresamos el factor de ampliacion
# n=int(input())

# En este caso n=3 , el factor de ampliacion es 3
n=3

# Ampliacion del cuadrado
for i in coordenadas:
    if (i[0]!=c1):
        i[0]*=n
    if (i[1]!=c2):
        i[1]*=n  
# Para dibujar la ampliacion le aumentamos los puntos de referencica y el punto de inicio
coordenadas.append(C)
coordenadas.append(A)

# Dibujamos el cuadrado y la ampliacion
j=[i[0] for i in coordenadas]
k=[i[1] for i in coordenadas]
plt.scatter(j,k)
plt.scatter(x,y)
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y)
plt.plot(j,k)
plt.show()