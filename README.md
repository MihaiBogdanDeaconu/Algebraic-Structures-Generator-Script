# Algebraic Structures Generator

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

---

A command-line tool for generating and enumerating fundamental algebraic structures. This project implements backtracking algorithms to systematically construct and validate **semigroups**, **Abelian groups**, and **subgroups** of direct products of cyclic groups. It was developed to translate abstract mathematical theory into concrete computational objects, providing a sandbox for exploring group theory.

## Core Functionality

-   **Semigroup Generation**: Generates all possible semigroups of a given order `n` by exhaustively searching for binary operations that satisfy the associativity property.
-   **Abelian Group Generation**: Constructs all Abelian groups of order `n`, leveraging key group properties (associativity, commutativity, Latin square property) to prune the search space efficiently.
-   **Subgroup Enumeration**: Identifies all subgroups of the direct product group `(ℤₘ × ℤₙ, +)` by finding all subsets closed under the group operation.

---

## Mathematical Background

The key to efficiently generating these structures was the use of mathematical properties, combined with recursive backtracking.

### 1\. Semigroup Generation

The script can generate all possible semigroups of a given order `n`. It utilizes a backtracking algorithm to systematically explore combinations of elements and verify **associativity** for each potential semigroup.

### 2\. Abelian Group Generation

Abelian Groups of a given order are recursively built using backtracking, using the structural properties of the operation table of a commutative (Abelian) group:

  - **Symmetry** with respect to the main diagonal.
  - **Element uniqueness** on each row and column.
  - The existence of the **identity element**.
  - Keeping its **associative nature**.

### 3\. Subgroup Enumeration

The script enumerates all subgroups of the Abelian Group `(ℤₘ × ℤₙ, +)`. For a finite group `(G, +)`, a non-empty subset `H` is a subgroup of `(G, +)` if and only if `H` is a stable subset of `(G,+)`. Hence, we check for closure under the operation.

## Project Structure

The project follows a modular structure to enforce separation of concerns, making the code clean, reusable, and easy to test.

```
algebraic-structures-generator/
├── data                           # Generated examples for various inputs
├── algebraic_structures/
│   ├── __init__.py
│   ├── semigroup_generator.py     # Core logic for semigroup generation
│   ├── abelian_group_generator.py # Core logic for Abelian group generation
│   ├── subgroup_generator.py      # Core logic for subgroup finding
│   └── utils.py                   # Helper functions for formatting output
├── main.py                        # Command-line interface and entry point
└── README.md                      # Project documentation
```

---

## Setup & Installation

Follow these steps to set up the project environment.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/MihaiBogdanDeaconu/Algebraic-Structures-Generator-Script.git
    cd algebraic-structures-generator
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
    *This project has no external dependencies, so no installation is required.*

---

## Usage

The tool is operated via the `main.py` script, which provides a command-line interface for accessing the different generators.

### 1. Generating Semigroups

To generate all semigroups of order `n=2` and save them to a file named `semigroups_n2.txt`:

```bash
python main.py semigroups 2 --output semigroups_n2.txt
```
**Example Output (`semigroups_n2.txt`):**
```
Operation table number 1: 
[ a₁ a₁ ]
[ a₁ a₁ ]

Operation table number 2: 
[ a₁ a₁ ]
[ a₁ a₂ ]

Operation table number 3: 
[ a₁ a₁ ]
[ a₂ a₂ ]

Operation table number 4: 
[ a₁ a₂ ]
[ a₁ a₂ ]

Operation table number 5: 
[ a₁ a₂ ]
[ a₂ a₁ ]

Operation table number 6: 
[ a₁ a₂ ]
[ a₂ a₂ ]

Operation table number 7: 
[ a₂ a₁ ]
[ a₁ a₂ ]

Operation table number 8: 
[ a₂ a₂ ]
[ a₂ a₂ ]

The total number of associative operations is 8
```

### 2. Generating Abelian Groups

To generate all Abelian groups of order `n=3` and save them to `abeliangroups_n3.txt`:

```bash
python main.py abeliangroups 3 --output abeliangroups_n3.txt
```
**Example Output (`abeliangroups_n3.txt`):**
```
Operation table number 1:
[ a₁ a₂ a₃ ]
[ a₂ a₃ a₁ ]
[ a₃ a₁ a₂ ]

Operation table number 2:
[ a₂ a₃ a₁ ]
[ a₃ a₁ a₂ ]
[ a₁ a₂ a₃ ]

Operation table number 3:
[ a₃ a₁ a₂ ]
[ a₁ a₂ a₃ ]
[ a₂ a₃ a₁ ]

The total number of Abelian Groups is 3
```

### 3. Finding Subgroups of ℤₘ × ℤₙ

To find all subgroups of the group `(ℤ₂ × ℤ₂, +)`:

```bash
python main.py subgroups 3 6 --output subgroups_z3z6.txt
```
**Example Output (`subgroups_z2z2.txt`):**
```
H1: ((0, 0), (0, 3))
H2: ((0, 0), (0, 3), (0, 1), (0, 2), (0, 4), (0, 5))
H3: ((0, 0), (0, 3), (0, 1), (0, 2), (0, 4), (0, 5), (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5))
H4: ((0, 0), (0, 3), (1, 0), (1, 3), (2, 0), (2, 3))
H5: ((0, 0), (0, 3), (1, 1), (1, 4), (2, 2), (2, 5))
H6: ((0, 0), (0, 3), (1, 2), (1, 5), (2, 1), (2, 4))
H7: ((0, 0), (0, 2), (0, 4))
H8: ((0, 0), (0, 2), (0, 4), (1, 0), (1, 2), (1, 4), (2, 0), (2, 2), (2, 4))
H9: ((0, 0), (1, 0), (2, 0))
H10: ((0, 0), (1, 2), (2, 4))
H11: ((0, 0), (1, 4), (2, 2))

The total number of subgroups of the abelian group (𝕫₃ x 𝕫₆, +) is 11

```
