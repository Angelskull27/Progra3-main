# test_solver.py

import os
from src.io_utils import load_puzzle_matrix, flatten_matrix
from src.sudoku_model import sudoku_csp
from src.search import backtracking_search
from src.propagators import ac3

PUZZLE_PATH = "test/puzzles/SD9DNXLH.txt"

def main():
    matrix = load_puzzle_matrix(PUZZLE_PATH)
    flat = flatten_matrix(matrix)

    csp = sudoku_csp(flat)
    ac3(csp)

    solution = backtracking_search(csp)

    if not solution:
        print("No se pudo resolver el sudoku.")
        return

    print("\n=== SUDOKU RESUELTO ===\n")
    pretty_print(solution)

def pretty_print(sol):
    for r in "ABCDEFGHI":
        row = [sol[r+c] for c in "123456789"]
        print(" ".join(row))

if __name__ == "__main__":
    main()
