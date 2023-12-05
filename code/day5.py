import numpy as np


def read_data(path):
    with open(path, "r") as file:
        seeds = [
            int(num) for num in file.readline().strip().split(":")[1].strip().split(" ")
        ]

    def line_to_int_list(line):
        return [int(x) for x in line.split()]

    # Dictionary to hold the data
    maps = {}
    current_map = None

    with open(path, "r") as file:
        for line in file:
            line = line.strip()
            if "map:" in line:
                # New map found, use it as the current key
                current_map = line.replace(":", "").strip()
                maps[current_map] = []
            elif line and current_map is not None:
                # Add the list of numbers to the current map
                maps[current_map].append(line_to_int_list(line))

    return seeds, maps


def split_into_pairs(lst):
    return [lst[i : i + 2] for i in range(0, len(lst), 2)]


def convert_pairs_to_ranges(lst):
    return [lst[0], lst[1] + lst[0]]


def create_ranges_from_mapping(mapping):
    return range(mapping[1], mapping[1] + mapping[2]), range(
        mapping[0], mapping[0] + mapping[2]
    )


def solution_1():
    min_location = np.inf
    for seed in seeds:
        for _, values in data_dict.items():
            for value in values:
                if value[1] <= seed < value[1] + value[2]:
                    seed = value[0] + seed - value[1]
                    break
        min_location = min(min_location, seed)
    return min_location


### Disclaimer: This does not work, but I am keeping it here for posterity
def solution_2(ranges):
    new = []
    while ranges:
        s, e = ranges.pop()
        for _, values in data_dict.items():
            for a, b, c in values:
                os = max(s, b)
                oe = min(e, b + c)
                if os < oe:
                    new.append((os - b + a, oe - b + a))
                    if os > s:
                        ranges.append((s, os))
                    if e > oe:
                        ranges.append((oe, e))
                    break
        else:
            new.append((s, e))
    ranges = new

    print(min(ranges)[0])


if __name__ == "__main__":
    seeds, data_dict = read_data("inputs/day5_input.txt")
    print(solution_1())
    seeds_range = []
    pairs = split_into_pairs(seeds)
    ranges = [convert_pairs_to_ranges(pair) for pair in pairs]
    solution_2(ranges)
    #   solution_2(ranges)
