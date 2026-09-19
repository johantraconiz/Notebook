# Clase 0 de CS50

## 1. Representación de Información y Abstracción del Hardware

* **La Primitiva Física (Bits y Transistores):** Las computadoras procesan información exclusivamente mediante **ceros y unos (bits)**, que físicamente representan la presencia o ausencia de electricidad regulada por **transistores**.
* **Sistema Binario (Base 2):** A diferencia del sistema decimal (base 10), la computación asigna pesos a cada posición mediante potencias de 2 (\\(2^0, 2^1, 2^2, \dots\\)).
* **Unidades y Estándares de Codificación:**
  * **Bytes:** Un grupo de 8 bits forma 1 byte, permitiendo representar \\(2^8 = 256\\) combinaciones distintas (de \\(0\\) a \\(255\\)).
  * **Texto (ASCII y Unicode):** Los estándares convierten patrones numéricos en caracteres. ASCII asigna valores a letras (con una diferencia fija de 32 entre mayúsculas y minúsculas), mientras que Unicode amplía la cantidad de bits para representar símbolos e idiomas globales.
  * **Imágenes (Modelo RGB):** Cada píxel se define con 3 bytes (uno para Rojo, Verde y Azul, con valores de 0 a 255 cada uno), lo que suma 24 bits por píxel.
  * **Multimedia:** El video es una abstracción construida mediante una secuencia rápida de imágenes estáticas (por ejemplo, 30 por segundo), mientras que el audio digital registra parámetros como frecuencia, duración y amplitud.

---

## 2. Pensamiento Algorítmico y Eficiencia

* **El Modelo Entrada/Salida:** La informática se define como el estudio de la resolución de problemas, donde un **algoritmo** actúa como la caja negra que procesa una entrada para generar una salida.
* **Diseño Algorítmico y Complejidad:** La ingeniería busca resolver problemas de forma correcta y eficiente en cuanto a uso de CPU y memoria RAM.
  * **Búsqueda Lineal:** Inspeccionar un elemento a la vez requiere un tiempo proporcional al tamaño del problema (\\(n\\)).
  * **Búsqueda Binaria (Divide y Vencerás):** Dividir el problema a la mitad de forma iterativa logra un rendimiento **logarítmico** (\\(\log n\\)). Esto permite procesar grandes volúmenes de datos agregando una cantidad mínima de pasos cuando el tamaño de los datos se duplica.

---

## 3. Bloques Fundamentales del Software

Cualquier programa informático se construye ensamblando primitivas básicas de programación:

* **Funciones:** Verbos o acciones que realizan un trabajo concreto e implementan un algoritmo en código.
* **Condicionales y Expresiones Booleanas:** Decisiones basadas en evaluaciones binarias de verdadero/falso (\\(1\\) o \\(0\\)).
* **Bucles (Loops):** Estructuras de repetición que permiten modularizar el código, evitar la duplicación y centralizar ajustes.
* **Variables y Valores de Retorno:** Contenedores de estado que permiten transferir datos de manera interna entre funciones.
* **Efectos Secundarios (Side Effects):** Manifestaciones externas derivadas de ejecutar una función, como mostrar texto en pantalla o emitir sonido.

---

## 4. Capas de Abstracción e Integración de IA

* **Compiladores e Intérpretes:** El software evoluciona creando capas sobre capas. Un **compilador** o intérprete traduce lenguajes de alto nivel (como Python) o bajo nivel (como C) a las instrucciones de máquina de ceros y unos.
* **APIs e Inteligencia Artificial:** La ingeniería moderna utiliza **APIs** para construir sobre soluciones existentes. Las herramientas de IA sirven como asistentes o copilotos, pero el ingeniero mantiene el rol de piloto que comprende la lógica de fondo para dirigir y validar la solución.
