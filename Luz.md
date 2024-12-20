# La Luz

La velicidad de la luz es constante

$$ c = 299.792.458 \text{ m/s} $$

Factor de Lorentz

$$ \gamma = \frac{1}{\sqrt{1-v^2/c^2}}$$

Corresponde al factor de Lorentz en la teoría de la relatividad especial de Albert Einstein. Este factor, γ, describe cómo el tiempo, la longitud y la masa de un objeto varían a medida que se mueve a velocidades cercanas a la velocidad de la luz (c).

El factor de Lorentz es esencial en varias ecuaciones relativistas, como la dilatación temporal y la contracción de la longitud, y se utiliza para ajustar las fórmulas de la física clásica (newtoniana) a contextos relativistas. Aquí:

- v es la velocidad del objeto.
- c es la velocidad de la luz en el vacío.

Cuando v se acerca a c, γ crece significativamente, lo que refleja efectos relativistas más intensos.

## Ecuaciones de Maxwell

- Ley de Gauss para el campo eléctrico:

$$ \nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0} $$

$$ \text{Esta ecuación describe cómo la densidad de carga eléctrica ρ genera un campo eléctrico E} $$

- Ley de Gauss para el campo magnético:

$$ \nabla \cdot \mathbf{B} = 0 $$

$$ \text{Esta ecuación establece que no existen monopolos magnéticos, es decir, las líneas de campo magnético B siempre forman bucles cerrados}$$

- Ley de Faraday de la inducción:

$$ \nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} $$

$$ \text{Esta ecuación describe cómo un campo magnético variable en el tiempo genera un campo eléctrico E} $$

- Ley de Ampère-Maxwell:

$$ \nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t} $$

$$\text{Esta ecuación muestra cómo una corriente eléctrica J y un campo eléctrico variable en el tiempo generan un campo magnético B} $$

## La Luz como partícula

Un fotón es la partícula de Luz parametrizada por la longitud de onda

$$ \lambda = \frac{c}{v}$$

Donde:

- $\lambda$ es la longitud de onda en metros
- $c$ es la velocidad de la luz en m/s
- $v$ es la frecuencia en Hz

Fórmula de la energía del fotón

$$ E = hv$$

Donde:

- $E$ es la energía del fotón en Joule
- $h$ es la constante de Plank ( $h=6.62607015×10^{−34} Js$, Julio segundos)
- $v$ es la frecuencia en Hz

## Luminosidad

Describe muchos fotones. Energía radiativa de una fuente bolométrico por longitud de onda y por frecuencia

$$L=\frac{\Delta E}{\Delta t} $$

$$ L_{\lambda}=\frac{\Delta E}{\Delta t \Delta \lambda} $$

## Flujo radiativo

$$f_\lambda = \frac{\Delta E}{\Delta t \Delta A \Delta\lambda}$$

Donde:

- $f_{\lambda}$ : es el Flujo en $Watts/m^2/m$
- $\Delta E$ : es la energía en Joule
- $\Delta t$ : es el tiempo en segundos
- $\Delta A$ : es el área en $m^2$
- $\Delta \lambda$ : es la longitud de onda en metros

## Cuerpo Negro

La **ecuación de Planck para el cuerpo negro** describe la radiación emitida por un cuerpo negro en equilibrio térmico a una temperatura determinada. Esta ecuación resolvió el problema de la **catástrofe ultravioleta**, una contradicción que surgió de la teoría clásica del electromagnetismo y la termodinámica, y fue un paso crucial en el desarrollo de la física cuántica.

### Ecuación de la ley de radiación de Planck

La expresión matemática que describe la **densidad espectral de radiación** emitida por un cuerpo negro a una temperatura \(T\), para una longitud de onda \(\lambda\), es:

$$
I(\lambda, T) = \frac{2hc^2}{\lambda^5} \cdot \frac{1}{e^{\frac{hc}{\lambda k_B T}} - 1}
$$

Donde:
- $I(\lambda, T)$ es la **intensidad** de la radiación emitida por unidad de área, por unidad de longitud de onda, a una temperatura (T),
- $h$ es la **constante de Planck**,
- $c$ es la **velocidad de la luz** en el vacío,
- $\lambda$ es la **longitud de onda** de la radiación,
- $k_B$ es la **constante de Boltzmann**,
- $T$ es la **temperatura absoluta** del cuerpo negro (en kelvins),
- $e$ es la base del logaritmo natural (aproximadamente 2.71828).

### Explicación de la ecuación

- Para **longitudes de onda largas** (infrarrojo), la radiación se comporta de acuerdo con la ley de Rayleigh-Jeans, lo que significa que la intensidad aumenta con la temperatura.
- Para **longitudes de onda cortas** (ultravioleta), la fórmula de Planck evita la "catástrofe ultravioleta" que predecía una cantidad infinita de radiación a frecuencias altas según la teoría clásica.
- La función decae exponencialmente en el ultravioleta, lo que explica por qué no se observa una explosión de energía en esas frecuencias.

### La catástrofe ultravioleta

Antes de la introducción de la ecuación de Planck, la ley de Rayleigh-Jeans, basada en la física clásica, predecía que la radiación de un cuerpo negro a frecuencias altas (en la región ultravioleta) crecía sin límite, lo que implicaba una cantidad infinita de energía emitida a frecuencias altas. Esto era claramente imposible y se conoció como la **catástrofe ultravioleta**.

Max Planck resolvió este problema al suponer que la energía de la radiación electromagnética solo podía emitirse o absorberse en **paquetes discretos** o **cuantos** de energía, en lugar de en cantidades continuas. Esto llevó al desarrollo de la mecánica cuántica.

### En resumen
La ecuación de Planck describe correctamente la radiación emitida por un cuerpo negro, ajustando tanto las regiones de baja frecuencia (donde coincide con la física clásica) como las de alta frecuencia (donde previene la catástrofe ultravioleta). Fue un descubrimiento fundamental que introdujo el concepto de la **cuantización** de la energía y marcó el nacimiento de la física cuántica.