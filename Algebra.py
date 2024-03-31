from itertools import product, permutations, combinations


class Algebra:
    global_count = 0
    translate_dictionary = {
        0: '₁',
        1: '₂',
        2: '₃',
        3: '₄',
        4: '₅',
        5: '₆',
        6: '₇',
        7: '₈',
        8: '₉',
        9: '₁₀',
        10: '₁₁',
        11: '₁₂',
        12: '₁₃',
        13: '₁₄',
        14: '₁₅',
        15: '₁₆',
        16: '₁₇',
        17: '₁₈',
        18: '₁₉',
        19: '₂₀',
    }

    def __init__(self):
        self.generated_subgroups = set()

    # Generate Semigroups
    def is_associative(self, table, n):
        """
        Description: Iterates over all operations with possible combinations of 3 elements, checking associativity by 
        checking the values from the table.(i.e (ab)c = a(bc) <=> table[table[a][b]][c] == table[a][table[b][c]]).
        Important! In most cases, the operation table is not complete, hence only the existing rows are tested.
        If the index gets out of range, we catch the error and continue iterating over the existing table. In the
        end, all the rows will be tested in case of a final solution.
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

    def is_done(self, solution, n):
        """
        Description: Tests if "solution" is a n x n table, case in which a solution was found, returning True,
        False otherwise.
        """
        if len(solution) == n:
            return True
        return False

    def backtrack_semigroups(self, n, solution, output_file):
        """
        Description: Recursive backtracking for generating all possible tables. 
        Approach: "elements(list)" will contain abstract elements(0, 1, ... up to n - 1),
        rather than a₁, a₂,..., in order to facilitate the use of indices in the operation table. "product(elements, repeat = n)"
        returns a list with all n - tuples created with elements from elements(repetitions allowed)(namely the Cartesian Product of (0,..., n - 1)^n).
        Starting from an empty "solution(table)", we append one row(one of the combinations 
        given by the Cartesian Product) at a time to the table, and check if the added row preserves associativity(1).
        (1.1) If it does, the following rows will be appended, tested and completed with combinations of elements from "elements",
        until a n x n matrix is created, meaning a solution was found. The last "valid" row gets popped, in order
        to test the next combination, and so on, until all the combinations were tested for all rows(if some rows
        don't preserve associativity, the next combination is chosen, to avoid redundant testing). (1.2) If a row doesn't
        preserve associativity, it is ignored.
        """
        elements = list(range(n))
        for combination in product(elements, repeat=n):
            solution.append(combination)
            if self.is_associative(solution, n):
                if self.is_done(solution, n):
                    self.print_operation_table(solution, output_file)
                else:
                    self.backtrack_semigroups(n, solution, output_file)
            solution.pop()

    def print_operation_table(self, table, output_file):
        """
        Description: Gets called when "solution" becomes a n x n table, meaning a solution was found.
        "print_operation_table(function)" counts the number of operation tables, then prints the table given
        as parameter is the format using a₁, a₂,..., aₙ and matrix format.
        """
        global global_count
        global_count += 1

        # Use UTF-8 encoding for elements' subscripts.
        with open(output_file, "a", encoding="utf-8") as file:
            file.write(f"Operation table number {global_count}: \n")
            for row in table:
                file.write("[ ")
                for elem in row:
                    file.write(f"a{self.translate_dictionary[elem]} ")
                file.write("]\n")
            file.write("\n")

    def clear_file(self, output_file):
        with open(output_file, "w"):
            pass

    def generateSemigroups(self):
        """
        Description: The main() iterates through all input files. These files contain 6 cases, n going from 1 to 5, plus an invalid case, when n = 0. The results for each
        case will be in the corresponding Output(test case).txt file. We suppose all input and output files exist and can be opened.
        """
        for i in range(1, 7):
            input_file = f"Input{i}.txt"
            output_file = f"Output{i}.txt"
            with open(input_file, "r") as file:
                try:
                    n = int(file.readline().strip())
                    if n < 1:
                        raise ValueError
                except:
                    with open(output_file, "w") as file:
                        file.write(
                            f"n must be a non-zero natural number or file couldn't be opened! Try again!\n")
                else:
                    global global_count
                    global_count = 0
                    solution = []
                    self.clear_file(output_file)
                    self.backtrack_semigroups(n, solution, output_file)
                    with open(output_file, "a") as file:
                        file.write(f"The total number of associative operations is {global_count}\n")

    # Generate Abelian Groups

    def is_commutative(self, solution, n):
        """
        Check if the given operation table is commutative.

        Args:
            solution (list of tuples): The operation table represented as a list of tuples.
            n (int): The order of the operation table.

        Returns:
            bool: True if the operation table is commutative, False otherwise.
        """
        for i in range(n):
            for j in range(n):
                try:
                    if (j >= i):
                        if (solution[i][j] != solution[j][i]):
                            return False
                except IndexError:
                    pass
        return True

    def uniqueElem(self, solution, n):
        """
        Check if each row of the operation table contains unique elements.

        Args:
            solution (list of tuples): The operation table represented as a list of tuples.
            n (int): The order of the operation table.

        Returns:
            bool: True if each row contains unique elements, False otherwise.
        """
        i = len(solution) - 1
        for j in range(n):
            for k in range(n):
                try:
                    if solution[k][j] == solution[i][j] and k != i:
                        return False
                except IndexError:
                    pass
        return True

    def is_consistent(self, solution, n):
        """
        Check if the operation table satisfies the requirements for an Abelian group.

        Args:
            solution (list of tuples): The operation table represented as a list of tuples.
            n (int): The order of the operation table.

        Returns:
            bool: True if the operation table satisfies the requirements, False otherwise.
        """
        return self.is_associative(solution, n) and self.is_commutative(solution, n) and self.uniqueElem(solution, n)

    def backtrack_abelian_groups(self, n, solution, output_file):
        """
        Generate Abelian groups of order n using backtracking.

        Args:
            n (int): The order of the Abelian group.
            solution (list): Current partial solution being explored.
            output_file (str): The name of the output file to write the results.
        """
        elements = list(range(n))
        arrangements = list(permutations(elements))
        for arrangement in arrangements:
            solution.append(arrangement)
            if self.is_consistent(solution, n):
                if self.is_done(solution, n):
                    self.print_operation_table(solution, output_file)
                else:
                    self.backtrack_abelian_groups(n, solution, output_file)
            solution.pop()

    def generateAbelianGroups(self):
        """
        Generate Abelian groups for each test case specified in the input files.
        """
        for i in range(1, 8):
            input_file = f"InputA{i}.txt"
            output_file = f"OutputA{i}.txt"
            with open(input_file, "r") as file:
                try:
                    n = int(file.readline().strip())
                    if n < 1:
                        raise ValueError
                except:
                    with open(output_file, "w") as file:
                        file.write(
                            f"n must be a non-zero natural number or file couldn't be opened! Try again!\n")
                else:
                    global global_count
                    global_count = 0
                    solution = []
                    self.clear_file(output_file)
                    self.backtrack_abelian_groups(n, solution, output_file)
                    with open(output_file, "a") as file:
                        file.write(f"The total number of Abelian Groups is {global_count}\n")

    # Generate the number of soubgroups of the abelian group (𝕫ₘ x 𝕫ₙ, +)

    def is_consistent_subgroup(self, solution, m, n):
        """
        Check if the given subset forms a consistent subgroup of the Abelian group Zₘ × Zₙ.

        Args:
            solution (list of tuples): The subset represented as a list of tuples.
            m (int): The modulus for the first component of elements in Zₘ.
            n (int): The modulus for the second component of elements in Zₙ.

        Returns:
            bool: True if the subset forms a consistent subgroup, False otherwise.
        """
        subgroup = set(solution)
        for i in subgroup:
            for j in subgroup:
                addition = ((i[0] + j[0]) % m, (i[1] + j[1]) % n)
                if addition not in subgroup:
                    return False
        return True

    def print_subgroups(self, solution, output_file):
        """
        Print the subgroup to the specified output file.

        Args:
            solution (list of tuples): The subgroup represented as a list of tuples.
            output_file (str): The name of the output file to write the results.
        """
        global global_count

        subgroup = tuple(sorted(solution))  
        if subgroup not in self.generated_subgroups:
            self.generated_subgroups.add(subgroup)
            global_count += 1
            with open(output_file, "a") as file:
                file.write(f"H{global_count}: (")
                for pair in solution:
                    file.write(f"{pair}")
                    if solution.index(pair) != len(solution) - 1:
                        file.write(", ")
                file.write(")\n")

    def backtrack_subgroups(self, m, n, solution, output_file):
        """
        Backtrack to generate all possible subgroups of the Abelian group Zₘ × Zₙ.

        Args:
            m (int): The modulus for the first component of elements in Zₘ.
            n (int): The modulus for the second component of elements in Zₙ.
            solution (list): Current partial solution being explored.
            output_file (str): The name of the output file to write the results.
        """
        elementsZm = list(range(m))
        elementsZn = list(range(n))
        pairs = list(product(elementsZm, elementsZn))

        for i in range(len(pairs)):
            for subset in combinations(pairs, i + 1):
                if all(pair not in solution for pair in subset):
                    solution.extend(subset)
                    if self.is_consistent_subgroup(solution, m, n):
                        self.print_subgroups(solution, output_file)
                        self.backtrack_subgroups(m, n, solution, output_file)
                    for _ in subset:
                        solution.pop()

    def generateSubgroups(self):
        """
        Generate all subgroups of the Abelian group Zₘ × Zₙ for each test case specified in the input files.
        """
        for i in range(6, 7):
            input_file = f"InputS{i}.txt"
            output_file = f"OutputS{i}.txt"
            with open(input_file, "r") as file:
                try:
                    m, n = map(int, file.readline().strip().split())
                    if m < 1 or n < 1:
                        raise ValueError(
                            "m and n must be non-zero natural numbers")
                except:
                    with open(output_file, "w", encoding="utf-8") as file:
                        file.write(
                            f"m and n must be a non-zero natural number or file couldn't be opened! Try again!\n")
                else:
                    global global_count
                    global_count = 0
                    solution = []
                    self.clear_file(output_file)
                    self.backtrack_subgroups(m, n, solution, output_file)
                    with open(output_file, "a", encoding="utf-8") as file:
                        file.write(
                            f"The total number of subgroups of the abelian group (𝕫ₘ x 𝕫ₙ, +) is {global_count}.\n")
