"""Command-line interface for generating algebraic structures."""

import argparse
import os
from algebraic_structures.semigroup_generator import generate_semigroups
from algebraic_structures.abelian_group_generator import generate_abelian_groups
from algebraic_structures.subgroup_generator import find_subgroups
from algebraic_structures.utils import format_operation_table, format_subgroup

def handle_semigroups(args):
    """Handler for the 'semigroups' command."""
    print(f"Generating semigroups of order n={args.n}...")
    try:
        solutions = generate_semigroups(args.n)
        with open(args.output, "w", encoding="utf-8") as f:
            for i, table in enumerate(solutions):
                f.write(f"Operation table number {i+1}:\n")
                f.write(format_operation_table(table))
                f.write("\n\n")
            f.write(f"The total number of associative operations is {len(solutions)}\n")
        print(f"Success! Results written to {args.output}")
    except Exception as e:
        print(f"An error occurred: {e}")

def handle_abelian_groups(args):
    """Handler for the 'abeliangroups' command."""
    print(f"Generating Abelian groups of order n={args.n}...")
    try:
        solutions = generate_abelian_groups(args.n)
        with open(args.output, "w", encoding="utf-8") as f:
            for i, table in enumerate(solutions):
                f.write(f"Operation table number {i+1}:\n")
                f.write(format_operation_table(table))
                f.write("\n\n")
            f.write(f"The total number of Abelian Groups is {len(solutions)}\n")
        print(f"Success! Results written to {args.output}")
    except Exception as e:
        print(f"An error occurred: {e}")

def handle_subgroups(args):
    """Handler for the 'subgroups' command."""
    print(f"Finding subgroups of (Z_{args.m} x Z_{args.n}, +)...")
    try:
        subgroups = find_subgroups(args.m, args.n)
        with open(args.output, "w", encoding="utf-8") as f:
            for i, subgroup in enumerate(subgroups):
                f.write(f"H{i+1}: {format_subgroup(subgroup)}\n")
            f.write(f"\nThe total number of subgroups is {len(subgroups)}.\n")
        print(f"Success! Results written to {args.output}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Main function to parse arguments and run the correct generator."""
    parser = argparse.ArgumentParser(
        description="A tool to generate various algebraic structures."
    )
    subparsers = parser.add_subparsers(required=True, dest='command')

    parser_sg = subparsers.add_parser(
        "semigroups", help="Generate semigroups of order n."
    )
    parser_sg.add_argument(
        "n", type=int, help="The order of the semigroup."
    )
    parser_sg.add_argument(
        "-o", "--output", type=str, default="semigroups_output.txt",
        help="Path to the output file."
    )
    parser_sg.set_defaults(func=handle_semigroups)

    parser_ag = subparsers.add_parser(
        "abeliangroups", help="Generate Abelian groups of order n."
    )
    parser_ag.add_argument(
        "n", type=int, help="The order of the Abelian group."
    )
    parser_ag.add_argument(
        "-o", "--output", type=str, default="abeliangroups_output.txt",
        help="Path to the output file."
    )
    parser_ag.set_defaults(func=handle_abelian_groups)

    parser_sub = subparsers.add_parser(
        "subgroups", help="Find subgroups of (Zm x Zn, +)."
    )
    parser_sub.add_argument(
        "m", type=int, help="The order of the Zm component."
    )
    parser_sub.add_argument(
        "n", type=int, help="The order of the Zn component."
    )
    parser_sub.add_argument(
        "-o", "--output", type=str, default="subgroups_output.txt",
        help="Path to the output file."
    )
    parser_sub.set_defaults(func=handle_subgroups)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()