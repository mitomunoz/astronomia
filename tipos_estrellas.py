import numpy as np
import matplotlib.pyplot as plt

# Constantes
h = 6.62607015e-34  # Constante de Planck (J·s)
c = 3.0e8           # Velocidad de la luz en el vacío (m/s)
k_B = 1.380649e-23  # Constante de Boltzmann (J/K)

# Función de la ley de radiación de Planck
def planck_law(lambda_, T):
    return (2 * h * c**2) / (lambda_**5) * (1 / (np.exp((h * c) / (lambda_ * k_B * T)) - 1))

# Definir las longitudes de onda (en metros)
wavelengths = np.linspace(1e-9, 3e-6, 1000)  # De 1 nm a 3 μm

# Nuevas temperaturas basadas en la clasificación espectral completa de estrellas
temperatures = {
    'Tipo O': 30000,  # Azul
    'Tipo B': 15000,  # Azul-blanco
    'Tipo A': 10000,  # Blanco
    'Tipo F': 7500,   # Blanco-amarillo
    'Tipo G': 6000,   # Amarillo
    'Tipo K': 4500,   # Naranja
    'Tipo M': 3000    # Rojo
}

# Colores correspondientes para cada tipo espectral
colors = {
    'Tipo O': 'blue',
    'Tipo B': 'cyan',
    'Tipo A': 'lightblue',
    'Tipo F': 'green',
    'Tipo G': 'yellow',
    'Tipo K': 'orange',
    'Tipo M': 'red'
}

# Graficar las intensidades para cada tipo espectral
plt.figure(figsize=(10, 6))

for star_type, T in temperatures.items():
    intensity = planck_law(wavelengths, T)
    plt.plot(wavelengths * 1e9, intensity, label=f'{star_type}: T = {T} K', color=colors[star_type])

# Añadir etiquetas y leyenda
plt.title('Ley de Radiación de Planck para Estrellas de Diferentes Tipos Espectrales')
plt.xlabel('Longitud de onda (nm)')
plt.ylabel('Intensidad (W·sr⁻¹·m⁻³)')
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()
