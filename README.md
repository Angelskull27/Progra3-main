🧩 ProgIIIG1-Sudoku

Resolución de Sudokus 9x9 mediante Programación con Restricciones (CSP)
Python 3.10+

Este proyecto implementa un resolutor completo de Sudokus mediante CSP, utilizando:

-Consistencia de arcos (AC-3)

-Forward Checking (FC)

-MAC (Maintaining Arc Consistency)

-Búsqueda por Backtracking con heurísticas

-Lectura de tableros desde archivos ```.txt```

-Tests automáticos

-Compatible con tableros de SudokuMania.com.ar, niveles desde Fácil hasta Imposible.

📂 Estructura del Proyecto
```
ProgIIIG1-Sudoku/
│
├── src/
│   ├── csp.py              # Clase CSP base
│   ├── sudoku_model.py     # Modelado del Sudoku como CSP
│   ├── propagators.py      # AC3, FC, MAC
│   ├── search.py           # Backtracking + heurísticas
│   └── io_utils.py         # Cargar y guardar tableros
│
├── test/
│   ├── puzzles/
│   │   ├── SD9DNXLH.txt
│   │   ├── SD9QWWU.txt
│   │   └── ... más sudokus
│   │
│   └── test_solver.py      # Script principal para resolver
│
└── README.md               # Este documento
```

📌 Formato de los Sudokus (.txt)

Cada archivo debe contener 9 líneas, cada una con 9 números separados por espacios.

Los ceros (```0```) representan casillas vacías.

Ejemplo válido:
```
7 0 0 8 0 0 0 0 0
0 2 1 6 3 0 8 0 7
0 6 2 0 0 9 0 0 1
3 0 0 0 0 0 9 0 8
6 0 0 0 0 0 0 2 5
0 2 0 8 0 5 0 0 0
0 0 0 0 0 0 0 0 6
0 9 0 0 0 0 0 0 0
0 0 5 3 0 0 0 0 2
```
🚀 Cómo Ejecutar el Solver

1️⃣ Ubícate en la carpeta raíz:
```
cd ProgIIIG1-Sudoku
```
2️⃣ Ejecuta el solver con Python usando el módulo de tests:
```
python -m test.test_solver
```

Esto cargará los puzzles de ```/test/puzzles/```, los resolverá e imprimirá:

-Tablero inicial

-Tablero resuelto

-Número de nodos explorados

-Tiempo de ejecución

3️⃣ Para resolver un puzzle específico
```
python -m test.test_solver --file test/puzzles/SD9DNXLH.txt
```
4️⃣ Elegir el método de consistencia
```
python -m test.test_solver --mode ac3
python -m test.test_solver --mode fc
python -m test.test_solver --mode mac
```
🔧 Descripción de los Módulos

📌 ```csp.py```

Contiene la estructura base del CSP:

-Variables

-Dominios

-Vecinos

-Función de restricción

-No incluye heurísticas, solo estructura.

📌 ```sudoku_model.py```

Modelado del Sudoku como CSP:

-Variables: A1…I9

-Dominios: {1…9}

-Restricción: celdas vecinas no pueden repetir valor

-Conversión desde un vector plano

-Función ```display()``` para imprimirlo

📌 ```propagators.py```

Implementa las técnicas de consistencia:

-AC-3

-revise()

-Forward Checking (FC)

-MAC

-Optimizado para la estructura del CSP usada en este proyecto.

📌 ```search.py```

Backtracking search con:

-MRV (Minimum Remaining Values)

-Degree Heuristic

-LCV para orden de valores

-Integración opcional de AC-3, FC o MAC

📌 ```io_utils.py```

Maneja:

-Lectura de puzzles desde ```.txt```

-Flatten 9x9 → lista de 81 valores

-Conversión a string

📌 ```test_solver.py```

Script de prueba y ejecución:

-Carga puzzles automáticamente

-Aplica el método de consistencia seleccionada

-Imprime el tablero resuelto

-Cuenta nodos de búsqueda

📈 Ejemplo de Salida
```
Cargando puzzle test/puzzles/SD9DNXLH.txt
Método: AC3 + Backtracking

Puzzle inicial:
7 . . 8 . . . . .
. 2 1 6 3 . 8 . 7
...

Puzzle resuelto:
7 8 9 8 4 2 5 1 3
...

Nodos explorados: 51
Tiempo: 0.031s
```
🧪 Añadir nuevos puzzles

Solo copia un archivo ```.txt``` a:

```test/puzzles/```


y ejecútalo con:

```python -m test.test_solver --file test/puzzles/MiPuzzleNuevo.txt```

🎓 Créditos

Proyecto desarrollado para el curso Programación III

Modelado CSP + Solución de Sudokus 9x9 usando técnicas de IA clásica.
