# Búsqueda Secuencial en Conjunto de Datos (50k)

Este proyecto implementa el algoritmo de **Búsqueda Secuencial** en Python. El programa procesa un archivo de texto con 50,000 números, los ordena y permite al usuario realizar búsquedas midiendo el tiempo de ejecución en milisegundos.

## 🚀 Análisis de Complejidad

La búsqueda secuencial es uno de los algoritmos más sencillos, pero su eficiencia depende directamente del tamaño de la entrada ($n$).

* **Peor caso $O(n)$:** Ocurre cuando el elemento buscado es el último de la lista o no se encuentra en ella. Se deben realizar $n$ comparaciones.
* **Caso promedio $O(n/2)$:** En promedio, se espera encontrar el elemento a la mitad de la lista.
* **Mejor caso $O(1)$:** Ocurre cuando el elemento buscado es el primero en la lista.
* **Complejidad Espacial:** $O(1)$ adicional, ya que no requiere estructuras de datos extra para la búsqueda más allá de la lista original.

## 💡 Casos de Uso

¿Cuándo es recomendable usar la búsqueda secuencial?
1.  **Listas no ordenadas:** Es el único método efectivo si los datos no tienen un orden específico.
2.  **Conjuntos de datos pequeños:** Para listas con pocos elementos, la diferencia de tiempo con métodos más complejos es despreciable.
3.  **Simplicidad:** Cuando se requiere una implementación rápida y fácil de depurar sin importar el rendimiento extremo.
4.  **Búsqueda única:** Si solo vas a buscar un elemento una sola vez, a veces no vale la pena el costo computacional de ordenar la lista para usar algoritmos más rápidos.

## 📊 Comparativa Teórica: Búsqueda Secuencial vs. Búsqueda Binaria

| Característica | Búsqueda Secuencial | Búsqueda Binaria |
| :--- | :--- | :--- |
| **Complejidad** | $O(n)$ (Lineal) | $O(\log n)$ (Logarítmica) |
| **Estado de la lista** | No requiere orden | **Obligatorio** que esté ordenada |
| **Eficiencia** | Baja en listas grandes | Muy alta en listas grandes |
| **Lógica** | Compara uno por uno | Divide el rango de búsqueda a la mitad |

**Conclusión:** Aunque en este programa ordenamos los datos, la búsqueda secuencial no aprovecha ese orden. En un escenario real con 50,000 datos ya ordenados, la **Búsqueda Binaria** sería significativamente más rápida, reduciendo las 50,000 comparaciones máximas a solo unas 16 aproximadamente.
