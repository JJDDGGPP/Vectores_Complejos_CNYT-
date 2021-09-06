# Librería de vectores complejos + unittest

Trabajo desarrollado en Python que proporciona una librería de distintas operaciones de vectores complejos como las siguientes:

1. Adición de vectores complejos.
2. Inverso (aditivo) de un vector complejo.
3. Multiplicación de un escalar por un vector complejo.
4. Adición de matrices complejas.
5. Inversa (aditiva) de una matriz compleja.
6. Multiplicación de un escalar por una matriz compleja.
7. Transpuesta de una matriz/vector.
8. Conjugada de una matriz/vector.
9. Adjunta (daga) de una matriz/vector.
10. Producto de dos matrices (de tamaños compatibles).
11. Función para calcular la "acción" de una matriz sobre un vector.
12. Producto interno de dos vectores.
13. Norma de un vector.
14. Distancia entre dos vectores.
15. Revisar si una matriz es Hermitiana.
16. Producto tensor de dos matrices/vectores.

## Comenzando 

### Pre-requisitos

Python 3.7.7

### Instalación

Descargue Python 3.7.7 de un sitio oficial y luego copie el archivo llamado *complexvectors.py* en donde quiera utilizar la librería.

 ## Ejemplos

Estos son ejemplos de como utilizar todas las funciones implementadas. Recuerde que si importaron complexvectors deben utilizar complexvectors. antes del nombre de cada función, este nombre puede cambiar si lo importaron y le cambiaron el nombre de la siguiente manera: 

```python
import complexvectors as cc
```

En este caso seria cc. y la función.

```python
sum_vect([9 + 7j, 11 + 0j, 14 - 18j], [6 + 3j, 3 + 1j, 10 - 8j])
inv_vect([9 + 7j, -4j, 14 - 18j])
vect_escalar([(-9 - 7j), (-11 + 0j), (-14 + 18j)], 4)
sum_matrix_comp([[4 + 8j, 7 + 1j, 8 + 4j], [4j, 6j, 7 - 8j]],
                  [[6 + 3j, 3 + 1j, 10 - 8j], [-8j, 4 + 10j, 2 - 1j]])
inv_matrix([[4 + 8j, 7 + 1j, 8 + 4j], [4j, 6j, 7 - 8j]])
matrix_escalar([[6 + 3j, 3 + 1j, 10 - 8j], [-8j, 4 + 10j, 2 - 1j]], 4)
trans([[4 + 8j, 7 + 1j, 8 + 4j], [4j, 6j, 7 - 8j]])
conjg([[4 + 8j, 7 + 1j, 8 + 4j], [4j, 6j, 7 - 8j]])
matrix_adj([[4 + 8j, 7 + 1j, 8 + 4j], [4j, 6j, 7 - 8j]])
matrix_matrix([[4 + 8j, 4j, 8 - 3j], [7 + 1j, 6j, 4 + 5j], [8 + 4j, 7 - 8j, 10]], [[6 + 3j, -8j, 5], [3 + 1j, 4 + 10j, 9j], [10 - 8j, 2 - 1j, 10 + 4.5j]])
prod_int_vect([4 + 8j, 4j, 8 - 3j], [8 + 4j, 7 - 8j, 10])
norma([(4, 5), (3, 1), (0, -7)])
distancia_vecotres([(3, 8), (5, -2), (8, -10)], [(8, 9), (3, -7), (6, 14)])
hermitian([[(3 + 0j), (2 - 1j), (-3j)], [(2 + 1j), (0 + 0j), (1 - 1j)], [(0 + 3j), (1 + 1j), (0 + 0j)]])
```



## Ejecutando las pruebas 

Para ejecutar las pruebas abra el archivo *unitest.py* y ejecútelo por consola o IDE.

### Analice las pruebas end-to-end

Esta prueba unittest nos permite verificar que la librería este correcta comparando los resultados de esta con valores resultados de las operaciones de vectores complejos.

## Construido con 

- [PyCharm]([PyCharm: el IDE de Python para desarrolladores profesionales, por JetBrains](https://www.jetbrains.com/es-es/pycharm/)) - IDE utilizado para el desarrollo de la librería y el test.
- [Python 3.7.7]([Welcome to Python.org](https://www.python.org/)) - Lenguaje de la librería.

## Autores 

- **Luis Felipe Giraldo** -  [Larfg]([Larfg (github.com)](https://github.com/Larfg))
