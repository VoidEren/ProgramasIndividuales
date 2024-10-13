import numpy as np
import matplotlib.pyplot as plt

#Definimos el rango de valores
x = np.linespace(-5, 5, 100)
y = np.linespace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.linespace(0.1, 5, 100) #la z > 0 es para evitar el ln(0)

#Definimos la funcion
def g(x, y, z):
    return np.sin(x) + np.cos(y) + np.log(z)

#Calculamos valores de g
g_valores = g(x, y, z)

#Graficamos
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot_surface(x, y, g_valores, cmap = 'plasma', edgecolor = 'none')
ax.set_title("Grafica de g(x, y, z) = sin(x) + cos(y) + ln(z)")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_Zlabel('g(x, y, z)')
plt.show()