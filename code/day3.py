from common import read_input

SYMBOLS = ["$", "*", "/", "+", "&", "@", "#", "%", "=", "-"]

"""
Basic algorithm steps:
----------------------
1. Iterate over the matrix except the first and last row and column.
2. If the current symbol is in the list of symbols, get the 3x3 neighbourhood
    around the current symbol.
3. Iterate over the neighbourhood and get all numbers.
4. If we found a number use 2 pointers to get the begining and end of the number.
5. Concatenate the left, middle and right parts and return the number.
6. Sum all the numbers in the neighbourhood and return the sum.

Notes:
This algorithm will count a number multiple times if multiple digits of the number are
in the 3x3 neighbourhood of the symbol. To compensate for this we use a set.
This introduces a new problem. If we have 2 of the same number in 1 row,
 in the neighbourhood
of 2 different symbols, we would count the number only once.

"""


def get_neighbour_number(matrix: list[str], row: int, col: int, i: int, j: int) -> int:
    """Get the actual number if a number was found in the neighbourhood of a symbol.

    Get the number position in the array and start going left and right with 2 pointers.
    Do this until both ends reach the end of the array or
      they hit a symbol or '.' symbol.
    Concatenate the left, middle and right parts and return the number.
    """
    row_index = i - 1 + row
    start = [j - 1 + col][0]
    offset = 1
    left_str = ""
    right_str = ""
    middle = matrix[row_index][start]
    left_bound = False
    right_bound = False
    while True:
        if not left_bound:
            left = start - offset
        if not right_bound:
            right = start + offset
        if left < 0 and right >= len(matrix):
            break

        if left >= 0:
            if not matrix[row_index][left].isdigit():
                left_bound = True
                left = -1

            else:
                left_str = matrix[row_index][left] + left_str

        if right < len(matrix):
            if not matrix[row_index][right].isdigit():
                right_bound = True
                right = len(matrix)
            else:
                right_str += matrix[row_index][right]
        offset += 1

    return int(left_str + middle + right_str)


def calc_neighbours_sum(
    matrix: list[str], neighbours: list[list[str]], i: int, j: int
) -> int:
    """Calculate the sum of all numbers in the neighbourhood of a symbol.

    This would count a number multiple times
        if it is in the neighbourhood of multiple symbols
    or if one symbol has multiple digits of a number in its neighbourhood.
    This is why we use a set to store the numbers in the row and then sum them up.
    """
    total_row_sum = 0
    for row in range(len(neighbours)):
        nums_in_row = set()
        for col in range(len(neighbours[0])):
            if neighbours[row][col].isdigit():
                nums_in_row.add(get_neighbour_number(matrix, row, col, i, j))
        total_row_sum += sum(nums_in_row)
    return total_row_sum


def calc_neighbours_sum_2(
    matrix: list[str], neighbours: list[list[str]], i: int, j: int
) -> int:
    """Calculate the sum of the numbers
    if there are exactly 2 numbers in the neighbourhood."""
    nums_in_row = set()
    for row in range(len(neighbours)):
        for col in range(len(neighbours[0])):
            if neighbours[row][col].isdigit():
                num = get_neighbour_number(matrix, row, col, i, j)

                nums_in_row.add(num)
        if len(nums_in_row) == 2:
            return nums_in_row.pop() * nums_in_row.pop()
    return 0


def get_neighbours(matrix: list[str], row: int, col: int) -> list[list[str]]:
    """Get the 3x3 array around the arg indexes."""
    neighbours = []
    for i in range(row - 1, row + 2):
        row_vector = []
        for j in range(col - 1, col + 2):
            row_vector.append(matrix[i][j])
        neighbours.append(row_vector)
    return neighbours


def solution_1(matrix: list[str]) -> int:
    total_sum = 0
    n = len(matrix)
    m = len(matrix[0])
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if matrix[i][j] in SYMBOLS:
                neighbours = get_neighbours(matrix, i, j)
                total_sum += calc_neighbours_sum(matrix, neighbours, i, j)
    return total_sum


def solution_2(matrix: list[str]) -> int:
    total_sum = 0
    n = len(matrix)
    m = len(matrix[0])
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if matrix[i][j] == "*":
                neighbours = get_neighbours(matrix, i, j)
                total_sum += calc_neighbours_sum_2(matrix, neighbours, i, j)

    return total_sum


if __name__ == "__main__":
    path = "inputs/day3.txt"
    matrix = read_input(path)
    print(solution_1(matrix))
    print(solution_2(matrix))
