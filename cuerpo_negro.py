
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

# Temperaturas para las cuales graficaremos
T1 = 3000  # Temperatura en K (Ejemplo: estrella fría)
T2 = 6000  # Temperatura en K (Ejemplo: Sol)

# Calcular la intensidad para ambas temperaturas
intensity_T1 = planck_law(wavelengths, T1)
intensity_T2 = planck_law(wavelengths, T2)

# Graficar
plt.figure(figsize=(10, 6))
plt.plot(wavelengths * 1e9, intensity_T1, label=f'T = {T1} K', color='blue')
plt.plot(wavelengths * 1e9, intensity_T2, label=f'T = {T2} K', color='red')

# Añadir etiquetas y leyenda
plt.title('Ley de Radiación de Planck')
plt.xlabel('Longitud de onda (nm)')
plt.ylabel('Intensidad (W·sr⁻¹·m⁻³)')
plt.legend()
plt.grid(True)

# Mostrar la gráfica
plt.show()

#1. Instala las bibliotecas necesarias, si no las tienes ya, usando:
#   ```bash
#   pip install numpy matplotlib
#   ```
#
#2. Guarda el código en un archivo `.py` y ejecútalo. Esto generará la gráfica de la ley de radiación de Planck para las temperaturas especificadas (3000 K y 6000 K).
#
#Si tienes alguna duda sobre la ejecución, ¡hazme saber!