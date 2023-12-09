from common import read_input
import math


def process_input(input: list[str]) -> tuple[list[int], list[int]]:
    times = [int(time) for time in input[0].split(":")[1].split(" ") if time]
    distances = [int(dist) for dist in input[1].split(":")[1].split(" ") if dist]

    return times, distances


def transfer_input(times, distances) -> tuple[int, int]:
    times = [str(time) for time in times]
    distances = [str(dist) for dist in distances]

    return int("".join(times)), int("".join(distances))


def dist_traveled(speed: int, time: int) -> int:
    return speed * (time - speed)


def solution_1(times: list[int], distances: list[int]) -> int:
    possible_ways = []
    for time, distance in zip(times, distances):
        times_won = 0
        for i in range(0, time):
            if distance < (result := dist_traveled(i, time)):
                times_won += 1
        possible_ways.append(times_won)

    return math.prod(possible_ways)


def solution_2(time: int, distance: int) -> int:
    possible_ways = []
    times_won = 0
    for i in range(0, time):
        if distance < (result := dist_traveled(i, time)):
            times_won += 1
    possible_ways.append(times_won)

    return math.prod(possible_ways)


if __name__ == "__main__":
    input = read_input("inputs/day6.txt")
    times, distances = process_input(input)
    print(solution_1(times, distances))
    time, distance = transfer_input(times, distances)
    print(solution_2(time, distance))
