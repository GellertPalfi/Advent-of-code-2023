import numpy as np


def read_input(path: str) -> list[str]:
    paths = []
    subpath = []
    with open(path, "r") as f:
        for line in f.readlines():
            if line == "\n":
                paths.append(subpath)
                subpath = []
            else:
                subpath.append(line.strip())

        if subpath:
            paths.append(subpath)
    return paths


def compare_arrays_with_one_mismatch(arr1, arr2):
    mismatches = np.sum(arr1 != arr2)
    return mismatches == 1


def mirror(path: list[str]) -> tuple[int, int]:
    path_array = np.array([list(row) for row in path])

    vertical_mirror_index = 0
    for i in range(len(path_array) - 1):
        top, bottom = i, i + 1
        is_mirror = True

        while bottom < len(path_array) and top >= 0:
            if not np.array_equal(path_array[top], path_array[bottom]):
                is_mirror = False
                break

            top -= 1
            bottom += 1

        if is_mirror:
            vertical_mirror_index = i + 1
            break

    if vertical_mirror_index:
        return vertical_mirror_index, 0

    horizontal_mirror_index = 0
    for i in range(len(path_array[0]) - 1):
        left, right = i, i + 1
        is_mirror = True

        while right < len(path_array[0]) and left >= 0:
            if not np.array_equal(path_array[:, left], path_array[:, right]):
                is_mirror = False
                break

            left -= 1
            right += 1

        if is_mirror:
            horizontal_mirror_index = i + 1
            break

    return vertical_mirror_index, horizontal_mirror_index


### not my solution
def find_mirror(grid):
    for r in range(1, len(grid)):
        above = grid[:r][::-1]
        below = grid[r:]

        if (
            sum(
                sum(0 if a == b else 1 for a, b in zip(x, y))
                for x, y in zip(above, below)
            )
            == 1
        ):
            return r

    return 0


def solution_1(paths):
    total_sum = 0
    for index, path in enumerate(paths):
        reflections = mirror(path)
        print(reflections)
        total_sum += reflections[0] * 100 + reflections[1]
    return total_sum


def solution_2(paths):
    total_sum = 0
    for index, path in enumerate(paths):
        row = find_mirror(path)
        total_sum += row * 100

        col = find_mirror(list(zip(*path)))
        total_sum += col
    return total_sum


if __name__ == "__main__":
    input = read_input("inputs/day13.txt")
    print(solution_2(input))
