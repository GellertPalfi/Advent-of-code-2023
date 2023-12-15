from common import read_input


def split_input(path: str) -> list[str]:
    with open(path, "r") as f:
        values = f.read().split(",")
    return values


def calculate_hash(line: list[str]) -> int:
    hash_value = 0
    for char in line:
        hash_value += ord(char)
        hash_value *= 17
        hash_value = hash_value % 256
    return hash_value


def solution_1(input: list[str]) -> int:
    total_sum = 0
    for line in input:
        total_sum += calculate_hash(line)
    return total_sum


def solution_2(input: list[str]) -> int:
    boxes = {i: {} for i in range(256)}

    for line in input:
        if line.endswith("-"):
            letters = line[:-1]
            hash_value = calculate_hash(letters)
            boxes[hash_value].pop(letters, None)
        else:
            letters, num = line.split("=")
            hash_value = calculate_hash(letters)
            boxes[hash_value][letters] = int(num)

    total_sum = 0
    for hash_value, values in boxes.items():
        for index, value in enumerate(values.values()):
            total_sum += (hash_value + 1) * (index + 1) * value

    return total_sum


if __name__ == "__main__":
    input = split_input("inputs/day15.txt")
    processed_input = [line.strip() for line in input]
    print(solution_1(processed_input))
    print(solution_2(processed_input))
