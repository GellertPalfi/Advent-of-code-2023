from common import read_input

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
"""
DIRECTIONS = {"north": (-1, 0), "south": (1, 0), "east": (0, 1), "west": (0, -1)}
OPPOSITE_DIRECTIONS = {
    "north": "south",
    "south": "north",
    "east": "west",
    "west": "east",
}
NEXT_DIRECTIONS = {
    "|": {"north": "south", "south": "north"},
    "-": {"east": "west", "west": "east"},
    "L": {"north": "east", "east": "north"},
    "J": {"north": "west", "west": "north"},
    "7": {"south": "west", "west": "south"},
    "F": {"south": "east", "east": "south"},
}


def process_input(input: list[str]):
    return [list(line) for line in input]


def get_starting_pos(matrix: list[str]) -> tuple[int, int]:
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == "S":
                return (i, j)


def calculate_polygon_area(loop_positions: list[tuple[int, int]]) -> float:
    """Shoelace formula"""
    x, y = zip(*loop_positions)
    return 0.5 * abs(
        sum(x[i] * y[i - 1] - x[i - 1] * y[i] for i in range(len(loop_positions)))
    )


def solution_1(matrix: list[str]) -> int:
    loop_positions = []
    row, col = get_starting_pos(matrix)
    loop_positions.append((row, col))
    # i sneek peaked at the next tile,
    # otherwise you would need a method to check the neigbouring tiles
    # to determine the next tile
    col += 1
    next_tile = matrix[row][col]
    direction_we_went_to = "east"
    step_count = 1
    while next_tile != "S":
        loop_positions.append((row, col))
        step_count += 1
        opposite_direction = OPPOSITE_DIRECTIONS[direction_we_went_to]
        next_dir = NEXT_DIRECTIONS[next_tile][opposite_direction]
        next_offset = DIRECTIONS[next_dir]
        direction_we_went_to = next_dir
        row += next_offset[0]
        col += next_offset[1]
        next_tile = matrix[row][col]

    return step_count // 2, loop_positions


def solution_2(area: float, loop_size: int) -> int:
    """Pick's theorem"""
    return int(area - 0.5 * loop_size + 1)


if __name__ == "__main__":
    input = read_input("inputs/day10.txt")
    processed_input = process_input(input)
    solution, loop_positions = solution_1(processed_input)
    print(f"Solution 1: {solution}")
    sorted_loop_positions = sorted(loop_positions, key=lambda x: (x[0], x[1]))
    area = calculate_polygon_area(loop_positions)
    print(solution_2(area, len(loop_positions)))
