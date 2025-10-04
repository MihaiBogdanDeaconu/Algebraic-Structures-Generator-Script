"""Generates all Abelian groups of a given order n."""

from itertools import permutations

def _is_associative(table: list[tuple[int, ...]], n: int) -> bool:
    """Checks if a partially or fully completed Cayley table is associative."""
    for a in range(n):
        for b in range(n):
            for c in range(n):
                try:
                    if table[table[a][b]][c] != table[a][table[b][c]]:
                        return False
                except IndexError:
                    pass
    return True

def _is_commutative(table: list[tuple[int, ...]], n: int) -> bool:
    """Checks if the operation table is commutative."""
    for i in range(n):
        for j in range(i, n):
            try:
                if table[i][j] != table[j][i]:
                    return False
            except IndexError:
                pass
    return True

def _has_unique_column_elements(table: list[tuple[int, ...]], n: int) -> bool:
    """Checks if the last added row maintains column uniqueness (Latin square property)."""
    i = len(table) - 1
    for j in range(n):
        for k in range(n):
            try:
                if table[k][j] == table[i][j] and k != i:
                    return False
            except IndexError:
                pass
    return True

def _is_consistent(table: list[tuple[int, ...]], n: int) -> bool:
    """Checks if a partial table satisfies Abelian group properties."""
    return (
        _is_associative(table, n) and
        _is_commutative(table, n) and
        _has_unique_column_elements(table, n)
    )

def _backtrack_abelian_groups(
    n: int,
    solution: list[tuple[int, ...]],
    all_solutions: list[list[tuple[int, ...]]],
):
    """Recursively builds and validates Abelian groups using backtracking.

    Args:
        n: The order of the group.
        solution: The current partial operation table.
        all_solutions: A list to store all found valid group tables.
    """
    elements = list(range(n))
    arrangements = list(permutations(elements))
    for arrangement in arrangements:
        solution.append(arrangement)
        if _is_consistent(solution, n):
            if len(solution) == n:
                all_solutions.append(list(solution))
            else:
                _backtrack_abelian_groups(n, solution, all_solutions)
        solution.pop()

def generate_abelian_groups(n: int) -> list[list[tuple[int, ...]]]:
    """Generates all Abelian group operation tables of a given order.

    Args:
        n: The order of the Abelian group (a positive integer).

    Returns:
        A list of all valid Abelian group operation tables.
    """
    if n < 1:
        raise ValueError("Order n must be a positive integer.")

    all_solutions = []
    _backtrack_abelian_groups(n, [], all_solutions)
    return all_solutions