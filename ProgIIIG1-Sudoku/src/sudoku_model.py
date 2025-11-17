# sudoku_model.py
# Modelo para tu propio solver sin usar la librería AIMA ni CSP externos

ROWS = "ABCDEFGHI"
COLS = "123456789"

def cross(a, b):
    return [s + t for s in a for t in b]

cells = cross(ROWS, COLS)

# Unidades (filas, columnas, cajas)
row_units = [cross(r, COLS) for r in ROWS]
col_units = [cross(ROWS, c) for c in COLS]
box_units = [cross(rs, cs) for rs in ("ABC", "DEF", "GHI")
                         for cs in ("123", "456", "789")]

unitlist = row_units + col_units + box_units
units = {s: [u for u in unitlist if s in u] for s in cells}
neighbors = {s: set(sum(units[s], [])) - {s} for s in cells}


def sudoku_csp(flat_puzzle):
    """
    Construye la estructura del sudoku para los algoritmos de search.py
    y propagators.py.
    flat_puzzle debe ser una lista de 81 valores (strings).
    """

    variables = cells

    domains = {}
    for i, cell in enumerate(cells):
        val = flat_puzzle[i]
        if val == "0":
            domains[cell] = list("123456789")
        else:
            domains[cell] = [val]

    # Construimos la estructura equivalente a un CSP pero sin usar AIMA
    csp = {
        "variables": variables,
        "domains": domains,
        "neighbors": neighbors,
        "units": units
    }

    return csp


def display(assignment):
    """Imprime el tablero en formato bonito."""
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for r in ROWS:
        print("".join(
            assignment[r + c][0].center(width) +
            ("|" if c in "36" else "")
            for c in COLS
        ))
        if r in "CF":
            print(line)
