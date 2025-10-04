"""Finds all subgroups of the Abelian group (Zm x Zn, +)."""

from itertools import product, combinations

def _is_closed_subset(subset: set[tuple[int, int]], m: int, n: int) -> bool:
    """Checks if a subset is closed under the group operation.

    Args:
        subset: The set of elements to check.
        m: The modulus for the first component.
        n: The modulus for the second component.

    Returns:
        True if the subset is closed, False otherwise.
    """
    for i in subset:
        for j in subset:
            addition = ((i[0] + j[0]) % m, (i[1] + j[1]) % n)
            if addition not in subset:
                return False
    return True

def _backtrack_subgroups(
    m: int,
    n: int,
    solution: list[tuple[int, int]],
    generated_subgroups: set[tuple[tuple[int, int], ...]],
):
    """Recursively finds subgroups using the original backtracking logic.

    Args:
        m: The modulus for the first component (Z_m).
        n: The modulus for the second component (Z_n).
        solution: The current list of elements being explored.
        generated_subgroups: A set to store unique subgroups found.
    """
    pairs = list(product(range(m), range(n)))

    for i in range(len(pairs)):
        for subset in combinations(pairs, i + 1):
            if all(pair not in solution for pair in subset):
                solution.extend(subset)
                if _is_closed_subset(set(solution), m, n):
                    subgroup = tuple(sorted(solution))
                    if subgroup not in generated_subgroups:
                        generated_subgroups.add(subgroup)
                    _backtrack_subgroups(m, n, solution, generated_subgroups)
                for _ in subset:
                    solution.pop()

def find_subgroups(m: int, n: int) -> list[tuple[tuple[int, int], ...]]:
    """Finds all subgroups of the Abelian group (Z_m x Z_n, +).

    Args:
        m: The order of the first cyclic group Z_m.
        n: The order of the second cyclic group Z_n.

    Returns:
        A list of subgroups. Each subgroup is a sorted tuple of its elements.
    """
    if m < 1 or n < 1:
        raise ValueError("Orders m and n must be positive integers.")
        
    generated_subgroups = set()
    _backtrack_subgroups(m, n, [], generated_subgroups)
    
    return sorted(list(generated_subgroups), key=len)