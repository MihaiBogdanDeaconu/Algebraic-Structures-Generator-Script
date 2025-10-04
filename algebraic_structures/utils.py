"""Utility functions for formatting and printing algebraic structures."""

_SUBSCRIPT_MAP = {
    0: '₁', 1: '₂', 2: '₃', 3: '₄', 4: '₅',
    5: '₆', 6: '₇', 7: '₈', 8: '₉', 9: '₁₀',
    10: '₁₁', 11: '₁₂', 12: '₁₃', 13: '₁₄', 14: '₁₅',
    15: '₁₆', 16: '₁₇', 17: '₁₈', 18: '₁₉', 19: '₂₀',
}

def format_operation_table(table: list[tuple[int, ...]]) -> str:
    """Formats a Cayley table for printing.

    Args:
        table: A list of tuples representing the operation table.

    Returns:
        A string representation of the formatted table.
    """
    lines = []
    for row in table:
        formatted_row = " ".join(f"a{_SUBSCRIPT_MAP.get(elem, '')}" for elem in row)
        lines.append(f"[ {formatted_row} ]")
    return "\n".join(lines)

def format_subgroup(subgroup: tuple) -> str:
    """Formats a subgroup for printing.

    Args:
        subgroup: A tuple of pairs representing the subgroup elements.

    Returns:
        A string representation of the subgroup.
    """
    return str(subgroup).replace('[', '(').replace(']', ')')