def read_file(path: str) -> list[str]:
    with open(path, "r") as f:
        return [line.strip() for line in f.readlines()]


def solution_1(lines: list[str]) -> int:
    sum = 0
    for line in lines:
        digits = [char for char in line if char.isdigit()]
        if digits:
            sum += int(digits[0] + digits[-1])
    return sum


def solution_2(
    lines: list[str], lookup_table: dict[str, str], verbose: bool = False
) -> int:
    sum = 0
    for line in lines:
        first_pos = len(line)
        last_pos = -1
        first_found_value = None
        last_found_value = None

        for key, value in lookup_table.items():
            pos = line.find(key)
            if 0 <= pos < first_pos:
                first_pos, first_found_value = pos, value

            pos = line.rfind(key)
            if pos > last_pos:
                last_pos, last_found_value = pos, value

        for index, char in enumerate(line):
            if not char.isdigit():
                continue
            if index < first_pos:
                first_found_value = char
                first_pos = index
            if index > last_pos:
                last_found_value = char
                last_pos = index

        if verbose:
            print(sum)
            print(line)
            print(first_found_value, last_found_value)
            print("------------------")

        sum += int(first_found_value + last_found_value)
    return sum


if __name__ == "__main__":
    path = "inputs/day1_input.txt"
    lines = read_file(path)

    lookup_table: dict[str, str] = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    print(solution_2(lines, lookup_table))
