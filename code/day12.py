from common import read_input
import functools
import itertools


def process_input(input):
    processed_input = []
    for row in input:
        hot_springs, numbers = row.split(" ")
        nums = [int(num) for num in numbers.split(",")]
        processed_input.append((hot_springs, nums))
    return processed_input


@functools.cache
def count_arrangements(springs, numbers):
    # base cases
    if not springs and not numbers:
        return 1
    if not springs and numbers:
        return 0

    if springs[0] == ("."):
        return count_arrangements(springs[1:], numbers)
    if springs[0] == ("?"):
        answer = 0
        answer += count_arrangements(springs[1:], numbers)
        if not numbers:
            return answer
        counter = 0
        for char in springs:
            if char == "." or counter == numbers[0]:
                break
            counter += 1

        if counter == numbers[0] and (
            counter >= len(springs)
            or counter < len(springs)
            and springs[counter] != "#"
        ):
            answer += count_arrangements(springs[counter + 1 :], numbers[1:])
        return answer
    if springs[0] == ("#"):
        if not numbers:
            return 0
        counter = 0
        for char in springs:
            if char == "." or counter == numbers[0]:
                break
            counter += 1

        if counter == numbers[0] and (
            counter >= len(springs)
            or counter < len(springs)
            and springs[counter] != "#"
        ):
            return count_arrangements(springs[counter + 1 :], numbers[1:])
        return 0


def solution1(input):
    total_sum = 0
    for springs, numbers in input:
        springs_copy = tuple(springs)
        numbers_copy = tuple(numbers)
        total_sum += count_arrangements(springs_copy, numbers_copy)
    return total_sum


def solution2(input):
    total_sum = 0
    for springs, numbers in input:
        springs_copy = tuple("?".join([springs] * 5))
        numbers_copy = tuple(itertools.chain(*[numbers] * 5))
        total_sum += count_arrangements(springs_copy, numbers_copy)
    return total_sum


if __name__ == "__main__":
    input = read_input("inputs/day12.txt")
    processed_input = process_input(input)
    print(solution1(processed_input))
    print(solution2(processed_input))
