import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Rango de valores
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
x, y = np.meshgrid(x, y)
z = 1 - x - y 

# Definimos la función
def f(x, y, z):
    return (x**2 + y**2 + z**2) / (x + y + z)

# Calcular los valores de f
with np.errstate(divide='ignore', invalid='ignore'):
    f_valores = f(x, y, z)
    f_valores[np.abs(x + y + z) < 1e-5] = np.nan  # Evitar divisiones por cero

# Graficar
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, f_valores, cmap='viridis', edgecolor='none')
ax.set_title("Gráfica de f(x, y, z) = (x^2 + y^2 + z^2) / (x + y + z)")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('f(x, y, z)')
plt.show()
