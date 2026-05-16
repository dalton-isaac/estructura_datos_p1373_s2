# estructura_datos_p1373_s2
##Estructura de Datos
##El programa compila en Python, no hay requerimientos especiales.
# Comparación: Búsqueda Secuencial vs Binaria

## Descripción
Este programa busca un número dentro de una lista de 1,000,000 de elementos para comparar qué algoritmo es más rápido. El código está escrito de forma directa usando ciclos básicos (`for` y `while`), sin funciones.

## Pre-requisitos
* Tener instalado Python.

## Instrucciones
1. Ejecuta el archivo en tu consola: `python main.py`
2. Escribe un número cuando el programa te lo pida y presiona Enter.
3. El programa te mostrará si encontró el número y cuánto tiempo tardó cada método.

## Resultados de la Comparación
* **Búsqueda Secuencial:** Recorre la lista número por número. Es más lenta, especialmente si buscas un número que está al final del millón.
* **Búsqueda Binaria:** Como la lista está ordenada, busca cortando por la mitad en cada paso. Es muchísimo más rápida y encuentra el número en una fracción de segundo.
