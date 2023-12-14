import numpy as np

from common import read_input


def roll_rocks(input: list[list[str]]) -> list[list[str]]:
    processed_input = []
    for line in input:
        joined_line = "".join(line).split("#")
        sorted_lines = []
        for sub_line in joined_line:
            sorted_lines.append(sorted(sub_line, reverse=True))
        sorted_line = "#".join(["".join(sub_line) for sub_line in sorted_lines])
        processed_input.append(sorted_line)
    return processed_input


def transpose(input: list[list[str]]) -> list[list[str]]:
    return list(map(list, zip(*input)))


def rotate_arr(matrix: list[list[str]]) -> list[list[str]]:
    new_matrix = []
    for i in range(len(matrix[0])):
        li = list(map(lambda x: x[i], matrix))
        li.reverse()
        new_matrix.append(tuple(li))

    return new_matrix


def solution_1(input: list[list[str]]) -> int:
    total_sum = 0
    for index, line in enumerate(input):
        stones = line.count("O")
        total_sum += stones * (len(input) - index)
    return total_sum


def solution_2(input: list[list[str]]) -> int:
    seen = {tuple(input)}
    seen_arr = [input]
    iter = 0
    while True:
        iter += 1
        for _ in range(4):
            rolled_input = transpose(roll_rocks(transpose(input)))
            rotate = rotate_arr(rolled_input)
            input = tuple(rotate)
        if input in seen:
            break
        seen.add(tuple(input))
        seen_arr.append(input)
    first = seen_arr.index(input)
    cycle_length = len(seen_arr) - first

    final_state = seen_arr[(1000000000 - first) % cycle_length + first]
    return solution_1(final_state)


if __name__ == "__main__":
    input = read_input("inputs/day14.txt")
    transposed = transpose(input)
    processed_input = roll_rocks(transposed)
    transposed_processed_input = transpose(processed_input)
    print(solution_1(transposed_processed_input))
    print(solution_2(input))
