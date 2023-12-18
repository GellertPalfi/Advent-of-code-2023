from common import read_input

DIR = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}
COLOR_MAP = {0: "R", 1: "D", 2: "L", 3: "U"}


def preprocess_input(input: list[str]) -> list[list[str]]:
    directions = []
    colors = []
    for line in input:
        line = line.split(" ")
        directions.append((line[0], int(line[1])))
        colors.append(line[2].replace("(", "").replace(")", "").replace("#", ""))

    return directions, colors


def picks_theorem(area: float, loop_size: int) -> int:
    """Pick's theorem"""
    return int(area - 0.5 * loop_size + 1)


def calculate_polygon_area(loop_positions: list[tuple[int, int]]) -> float:
    """Shoelace formula"""
    x, y = zip(*loop_positions)
    return 0.5 * abs(
        sum(x[i] * y[i - 1] - x[i - 1] * y[i] for i in range(len(loop_positions)))
    )


def solution_1(directions: list[tuple[str, int]]) -> int:
    points = [(0, 0)]
    boundary_len = 0

    for row in directions:
        direction, steps = row
        dir_row, dir_col = DIR[direction]
        boundary_len += steps
        curr_row, curr_col = points[-1]
        points.append((curr_row + dir_row * steps, curr_col + dir_col * steps))

    area = int(calculate_polygon_area(points))

    return picks_theorem(area, boundary_len) + boundary_len


def solution_2(colors):
    directions = []

    for row in colors:
        value = int(row[:5], 16)
        dir = int(row[-1], 16)
        directions.append((COLOR_MAP[dir], value))

    return solution_1(directions)


if __name__ == "__main__":
    input = read_input("inputs/day18.txt")
    directions, colors = preprocess_input(input)

    print(solution_1(directions))
    print(solution_2(colors))
