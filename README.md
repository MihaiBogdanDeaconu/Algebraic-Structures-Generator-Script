# Algebraic-Structures-Generator-Script

## Description

This project is a Python script designed to generate various algebraic structures such as semigroups, Abelian groups, and subgroups of a given order. It provides functionalities to explore and enumerate different algebraic systems, offering insights into their properties and relationships. The key to efficiently generate this structures was the use of mathematical properties, combined with recursive backtracking.

## Features

### 1. Semigroups Generation

The script can generate all possible semigroups of a given order n. It utilizes a backtracking algorithm to systematically explore combinations of elements and verify associativity for each potential semigroup.

### 2. Abelian Groups Generation

Abelian Groups of a given order are recursively built using backtracking, using the structural property of the operation table of commutative groups(Abelian): 
- Symmetry with respect to the main diagonal
- Element uniqueness on row/column
- The existence of the identity element
- Keeping its associative nature

### 3. Subgroups Enumeration

The script enumerates all subgroups of the Abelian Group (Zₘ x Zₙ, +). For a finite group (G, +), a non-empty subset H is a subgroup of (G, +) if and only if H is a stable subset of (G,+). Hence, we checked and existence of the identity element and the stability.

## Usage

### To utilize the functionalities of this script, follow these steps:

1.Prepare input files (Input*.txt) containing the desired parameters for generating algebraic structures.

2.Run the script, specifying the appropriate input file corresponding to the desired operation.

3.The script will generate output files (Output*.txt) containing the enumerated algebraic structures and relevant information.

Remark: In the "inputOutput" you can find various applied examples.

## Contribution

Contributions to this project are welcome! If you have ideas for improvements, additional features, or bug fixes, feel free to submit a pull request or open an issue on GitHub.
