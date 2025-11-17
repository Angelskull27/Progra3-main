# io_utils.py

def load_puzzle_matrix(path):
    """Carga un sudoku en formato matriz 9x9 separado por espacios."""
    puzzle = []
    with open(path, "r") as f:
        for line in f:
            row = [int(v) for v in line.strip().split()]
            puzzle.append(row)
    return puzzle


def flatten_matrix(matrix):
    """Convierte matriz 9x9 → cadena linear de 81 caracteres."""
    return "".join(str(x) for row in matrix for x in row)
