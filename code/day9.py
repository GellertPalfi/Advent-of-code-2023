from common import read_input


def process_input(lines: list[str]) -> list[int]:
    processed_lines = []
    for line in lines:
        processed_lines.append([int(number) for number in line.split(" ")])
    return processed_lines


# 0 3 6 9 12 15
def get_next_element(line: str) -> int:
    differences = []
    for index in range(len(line) - 1):
        differences.append(line[index + 1] - line[index])
    if all(diff == 0 for diff in differences):
        return line[-1]
    else:
        return get_next_element(differences) + line[-1]


def solution_1(input: list[str]) -> int:
    total_sum = 0
    for line in input:
        total_sum += get_next_element(line)
    return total_sum


def solution_2(input: list[str]) -> int:
    total_sum = 0
    for line in input:
        reversed_line = line[::-1]
        total_sum += get_next_element(reversed_line)
    return total_sum


if __name__ == "__main__":
    input = read_input("inputs/day9.txt")
    processed_input = process_input(input)
    print(solution_1(processed_input))
    print(solution_2(processed_input))
