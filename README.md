Introducción
Este documento explica el funcionamiento de una aplicación de simulación desarrollada en Python con interfaz gráfica (GUI). La aplicación permite resolver dos problemas:

Simulación de comisiones en una agencia de automóviles.

Cálculo de utilidades en una venta callejera de pastelitos.

El código utiliza las bibliotecas Tkinter para la interfaz gráfica, NumPy para cálculos numéricos eficientes, y threading para evitar bloqueos durante simulaciones largas.

Estructura General
La aplicación se organiza en dos pestañas independientes, cada una con:

Campos para ingresar parámetros.

Botones para iniciar simulaciones.

Áreas de resultados (promedios, probabilidades, tablas).

Componentes Clave
1. Clase SimulationApp
Función __init__:

Inicializa la ventana principal y las pestañas.

Configura los elementos de la interfaz para cada problema.

2. Configuración de la Interfaz
Para la agencia de autos:

Campos de entrada: número de semanas (n), umbral de comisión (y), fila inicial (j), número de filas a mostrar (i).

Botón "Simular" que ejecuta run_agencia_simulation.

Resultados: comisión promedio, probabilidad de superar el umbral y, y tablas con datos específicos.

Para la venta callejera:

Campos de entrada: número de días (N), fila inicial (j), número de filas a mostrar (i).

Botón "Simular" que ejecuta run_venta_simulation.

Resultados: promedio de sobrantes diarios, utilidad promedio y tabla de estados.

Flujo de las Simulaciones
Agencia de Autos
Validación de entradas:

Verifica que los valores ingresados sean numéricos y coherentes (ej: j + i ≤ n).

Simulación en segundo plano:

Usa hilos (threading) para evitar bloquear la interfaz.

Lógica de comisiones:

Para cada vendedor (4 en total):

Determina cuántos autos vendió (distribución: 0-4 autos/semana).

Por cada auto, elige el tipo (compacto, mediano, lujo) y calcula la comisión según probabilidades.

Resultados:

Comisión promedio por vendedor.

Probabilidad de que un vendedor supere el umbral y.

Tabla con filas específicas (desde la fila j hasta j+i) y la última fila simulada.

Venta Callejera
Validación de entradas:

Similar a la agencia.

Simulación en segundo plano:

Genera datos diarios:

Número de clientes (entre 10 y 30).

Demanda por cliente (distribución: 1, 2, 5, 6, 7, 8, 10 unidades).

Precio variable según demanda (100 o 80 pesos).

Cálculos clave:

Sobrantes: 200 - demanda_total (si la demanda no supera 200).

Utilidad: Ingresos (demanda * precio) - Costos (200 * $30).

Resultados:

Sobrantes promedio por día.

Utilidad promedio diaria.

Tabla con filas específicas y última fila.

Gestión de Memoria y Rendimiento
Solo se almacenan filas críticas:

Las filas solicitadas por el usuario (desde j hasta j+i).

La última fila generada.

Uso de NumPy:

Acelera la generación de números aleatorios (ej: np.random.choice).

Hilos:

Permiten ejecutar simulaciones largas (ej: 100,000 iteraciones) sin congelar la interfaz.

Manejo de Errores
Validación de entradas:

Muestra mensajes de error si:

Los valores no son numéricos.

j + i excede el total de iteraciones.

Interfaz robusta:

Deshabilita botones durante la simulación para evitar ejecuciones múltiples.

Ejemplo de Uso
Agencia de Autos
Ingresar: n = 1000, y = 1500, j = 500, i = 10.

Hacer clic en "Simular".

Resultados:

Comisión promedio: Ej: $1200.50.

Probabilidad de comisión > $1500: Ej: 15.3%.

Tabla con 10 filas desde la semana 500.

Venta Callejera
Ingresar: N = 500, j = 200, i = 5.

Hacer clic en "Simular".

Resultados:

Sobrantes promedio: Ej: 25 unidades/día.

Utilidad promedio: Ej: $3500.00.

Tabla con 5 filas desde el día 200.

Conclusión
Esta aplicación permite modelar escenarios complejos de forma interactiva, mostrando resultados estadísticos y detalles específicos de manera eficiente. Su diseño modular facilita la extensión para añadir nuevas simulaciones o modificar parámetros existentes.

Requisitos: Python 3.x, bibliotecas Tkinter, NumPy.
