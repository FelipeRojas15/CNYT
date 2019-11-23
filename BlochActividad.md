# actividad-Bloch

### 1. Importación de librerías

```python
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
%matplotlib notebook  # Para interactuar con las gráficas  
```
### 2. Cómo graficar una esfera, un punto, una flecha y cómo hacer una etiqueta

```python
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

phi, theta = np.mgrid[0 : 2 * np.pi : 0.1, 0 : np.pi : 0.1]  # Equivale a hacer un doble for

# Para pasar de coordenadas esféricas (phi, theta) a coordenadas cartesianas (x, y, z):

x = np.cos(phi) * np.sin(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(theta)

# Para graficar la esfera (estructura de alambre):

ax.plot_wireframe(x, y, z, color='yellow', rstride=2, cstride=2, linewidth=0.5, alpha=0.8)

# Para graficar un punto cualquiera en el espacio 3d, en este caso (2, -2, 1):

ax.scatter(2, -2, 1, color='red', s=10) # El valor de s modifica el grosor del punto

# Para hacer una etiqueta, en este caso sobre el punto (2, -2, 1):

ax.text(2, -2, 1, 'Punto', color='black')

# Para graficar una flecha, en este caso del origen al punto (2, -2, 1):

ax.quiver(0, 0, 0, 2, -2, 1, color='blue')

# Nombres de los ejes

ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

plt.show()
```
### 3. Ejercicio de calentamiento

Grafique una esfera que representará el planeta Tierra. Grafique como puntos sobre la esfera cada una de las ciudades dadas, asegúrese de crear también una etiqueta con el nombre de la ciudad. Expanda la lista con 5 ciudades de su elección.

```python
# El formato de cada entrada de la lista es: [nomCiudades, Latitud, Longitud]

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
%matplotlib notebook  
import math


Ciudades = [
    ['Londres', 51.5, -0.1167],
    ['Bogotá', 4.5964, -74.0833],
    ['Roma', 41.8960, 12.4833],
    ['Melbourne', -37.8200, 144.9750],
    ['Nairobi', -1.2833, 36.8167],
    ['Santiago', -33.4500, -70.6670],
    ['Nueva York', 40.6943, -73.9249],
    ['Los Angeles', 34.1139, -118.4068],
    ['Moscú', 55.7522, 37.6155],
    ['Quito', -0.2150, -78.5001],
    ['Tokio', 35.6850, 139.7514],
    ['Lagos', 6.4433, 3.3915],
    ['Atenas', 37.9833, 23.7333],
    ['Belén de Pará', -1.4500, -48.4800],
    ['Budapest', 47.5000, 19.0833],
    ['Vancouver', 49.2734, -123.1216],
    ['París', 48.8667, 2.3333],
    ['Puebla', 19.0500, -98.2000],
    ['El Cairo', 30.0626300, 31.2496700],
    ['Bruselas', 50.8504500, 4.3487800],
    ['Zimbabwe', -20.0000000, 30.0000000]
]
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
phi, theta = np.mgrid[0 : 2 * np.pi : 0.1, 0 : np.pi : 0.1]  # Equivale a hacer un doble for

# Para pasar de coordenadas esféricas (phi, theta) a coordenadas cartesianas (x, y, z):

x = np.cos(phi) * np.sin(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(theta)

# Para graficar la esfera (estructura de alambre):

ax.plot_wireframe(x, y, z, color='green', rstride=2, cstride=2, linewidth=0.5, alpha=0.8)

for i in range(len(Ciudades)):
    nomCiudades = Ciudades[i][0]
    # Pasando de Grados a Radianes 
    Ciudades[i][2]=(Ciudades[i][2]*math.pi)/180
    
    # Pasando de Latitud geografica a Latitud Matematica 
    Ciudades[i][1]=((-Ciudades[i][1]+90)*math.pi)/180
    
    x1 = np.cos(Ciudades[i][2]) * np.sin(Ciudades[i][1])
    y1 = np.sin(Ciudades[i][2]) * np.sin(Ciudades[i][1])
    z1 = np.cos(Ciudades[i][1])
    
    # Para graficar un punto cualquiera en el espacio 3d, en este caso (x1, y1, z1):
    ax.scatter(x1, y1, z1, color='blue', s=10)
    
    ax.text(x1, y1, z1,nomCiudades , color='black')
    ax.quiver(0, 0, 0, x1, y1, z1, color='blue')


ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_zlabel('Eje Z')

plt.show()
```
imagen
