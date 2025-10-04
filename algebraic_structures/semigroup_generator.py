"""Generates all semigroups of a given order n."""

from itertools import product

def _is_associative(table: list[tuple[int, ...]], n: int) -> bool:
    """Checks if a partially or fully completed Cayley table is associative.

    Args:
        table: The current operation table.
        n: The order of the set.

    Returns:
        True if the table is associative given its current state, False otherwise.
    """
    for a in range(n):
        for b in range(n):
            for c in range(n):
                try:
                    if table[table[a][b]][c] != table[a][table[b][c]]:
                        return False
                except IndexError:
                    pass
    return True

def _backtrack_semigroups(
    n: int,
    solution: list[tuple[int, ...]],
    all_solutions: list[list[tuple[int, ...]]],
):
    """Recursively builds and validates semigroups using backtracking.

    Args:
        n: The order of the semigroup.
        solution: The current partial operation table being built.
        all_solutions: A list to store all found valid semigroup tables.
    """
    elements = list(range(n))
    for combination in product(elements, repeat=n):
        solution.append(combination)
        if _is_associative(solution, n):
            if len(solution) == n:
                all_solutions.append(list(solution))
            else:
                _backtrack_semigroups(n, solution, all_solutions)
        solution.pop()

def generate_semigroups(n: int) -> list[list[tuple[int, ...]]]:
    """Generates all semigroup operation tables of a given order.

    This function orchestrates the backtracking algorithm to find all valid
    associative binary operations on a set of n elements.

    Args:
        n: The order of the semigroup (a positive integer).

    Returns:
        A list of all valid semigroup operation tables. Each table is
        represented as a list of tuples.
    """
    if n < 1:
        raise ValueError("Order n must be a positive integer.")
    
    all_solutions = []
    _backtrack_semigroups(n, [], all_solutions)
    return all_solutions