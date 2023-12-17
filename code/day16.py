from collections import namedtuple
from copy import deepcopy
from operator import add

from common import read_input

DIR = {"north": (-1, 0), "south": (1, 0), "east": (0, 1), "west": (0, -1)}
OPPOSITE_DIRECTIONS = {
    "north": "south",
    "south": "north",
    "east": "west",
    "west": "east",
}
NEXT_DIRECTIONS = {
    "|": {
        "north": "south",
        "south": "north",
        "west": ["south", "north"],
        "east": ["south", "north"],
    },
    "-": {
        "east": "west",
        "west": "east",
        "north": ["west", "east"],
        "south": ["west", "east"],
    },
    "\\": {"north": "east", "east": "north", "south": "west", "west": "south"},
    "/": {"north": "west", "west": "north", "south": "east", "east": "south"},
    ".": {"north": "south", "east": "west", "west": "east", "south": "north"},
}


def process_input(input: list[str]):
    return [list(line) for line in input]


def in_bounds(grid, row, col):
    grid_width = len(grid[0])
    grid_height = len(grid)
    return 0 <= row < grid_height and 0 <= col < grid_width


Beam = namedtuple("Beam", ["current_pos", "dir"])


def energize(input, starting_pos, direction):
    energized_points = deepcopy(input)
    row, col = starting_pos
    curr_char = input[row][col]
    beams = []
    # next_dir can be a list if the first charachter splits the beam
    next_dir = NEXT_DIRECTIONS[curr_char][direction]
    if isinstance(next_dir, list):
        for dir in next_dir:
            beams.append(Beam(starting_pos, dir))
    else:
        beams.append(Beam(starting_pos, next_dir))
    seen = set()

    while beams:
        new_beams = []
        for beam in beams:
            row, col = beam.current_pos
            energized_points[row][col] = "#"
            next_row, next_col = map(add, beam.current_pos, DIR[beam.dir])

            # if the beam wont be in bounds on the next step
            # it can safely be discarded
            if not in_bounds(input, next_row, next_col):
                continue

            next_char = input[next_row][next_col]
            dir_we_came_from = OPPOSITE_DIRECTIONS[beam.dir]

            # next_dir can be a list if the first charachter splits the beam
            next_dirs = NEXT_DIRECTIONS[next_char][dir_we_came_from]

            if isinstance(next_dirs, list):
                for dir in next_dirs:
                    # create split beans
                    next_beam = Beam((next_row, next_col), dir)
                    # check if we already seen this beam
                    # this beam meaning the beam on this position
                    # and traveling the same direction
                    if next_beam not in seen:
                        new_beams.append(next_beam)
                        seen.add(next_beam)
            else:
                next_beam = Beam((next_row, next_col), next_dirs)
                if next_beam not in seen:
                    new_beams.append(next_beam)
                    seen.add(next_beam)

        beams = new_beams

    return energized_points


def solution_1(input: list[list[str]], starting_pos, direction) -> int:
    energized_input = energize(input, starting_pos, direction)
    return sum([line.count("#") for line in energized_input])


def solution_2(input_grid):
    def get_starting_positions(direction):
        if direction == "west":
            return [(i, 0) for i in range(len(input_grid))]
        elif direction == "north":
            return [(0, i) for i in range(len(input_grid[0]))]
        elif direction == "east":
            return [(i, len(input_grid[0]) - 1) for i in range(len(input_grid))]
        elif direction == "south":
            return [(len(input_grid) - 1, i) for i in range(len(input_grid[0]))]

    energised_cell_counts = []
    for direction in DIR:
        for starting_pos in get_starting_positions(direction):
            energised_cell_counts.append(
                solution_1(input_grid, starting_pos, direction)
            )

    return max(energised_cell_counts)


if __name__ == "__main__":
    input = read_input("inputs/day16.txt")
    processed_input = process_input(input)
    starting_pos = (0, 0)
    direction = "west"
    print(solution_1(processed_input, starting_pos, direction))
    print(solution_2(processed_input))
