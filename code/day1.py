from common import read_input


def solution_1(lines: list[str]) -> int:
    sum = 0
    for line in lines:
        # find all digits in the line
        digits = [char for char in line if char.isdigit()]
        if digits:
            # sum them up, this works also if there is only one digit,
            # because then digits[0] == digits[-1]
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

        # checking for spelled out numbers
        for key, value in lookup_table.items():
            # check if the line contains any spelled out numbers from the begining
            pos = line.find(key)
            # if yes, check if it is the first one
            if 0 <= pos < first_pos:
                first_pos, first_found_value = pos, value

            # check if the line contains any spelled out numbers from the end
            pos = line.rfind(key)
            # if yes, check if it is the last one
            if pos > last_pos:
                last_pos, last_found_value = pos, value

        # checking for digits
        for index, char in enumerate(line):
            if not char.isdigit():
                continue
            # we already looked for spelled out numbers,
            # so we know if there were any in the string
            # if yes compare their start positoins with the current start position
            # of the digit
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
    path = "inputs/day1.txt"
    lines = read_input(path)

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
