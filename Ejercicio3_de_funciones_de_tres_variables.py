import numpy as np
import matplotlib.pyplot as plt

#Rango de valores
x = np.linspace(-5, 5, 100)
y = np.linspace(5, -5, 100)
x, y = np.meshgrid(x, y)
z = np.linspace(0.1, 5, 100) #Evitamos z = 0 para que no haya division (0)

#Definimos funcion
def h(x, y, z):
    return (x * y) / z

#Calculamos los valores de h
h_valores = h(x, y, z)

#Graficamos
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot_surface(x, y, h_valores, cmap = 'coolwarm', edgecolor = 'none')
ax.set_title("Grafica de h(x, y, z) = (x * y) / z")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('h(x, y, z)')
plt.show()