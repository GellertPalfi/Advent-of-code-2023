from heapq import heappush, heappop

from common import read_input

DIR = {"north": (-1, 0), "south": (1, 0), "east": (0, 1), "west": (0, -1)}


def process_input(input: list[str]) -> list[list[str]]:
    return [list(map(int, line.strip())) for line in input]


def solution_1(input: list[int]) -> int:
    seen = set()
    # heatloss, row, col, dir_row, dir_col, number_of_steps
    queue = [(0, 0, 0, 0, 0, 0)]
    R = len(input)
    C = len(input[0])

    while queue:
        heatloss, row, col, dir_row, dir_col, no_steps = heappop(queue)

        if row == R - 1 and col == C - 1 and no_steps > 3:
            return heatloss

        if (row, col, dir_row, dir_col, no_steps) in seen:
            continue

        seen.add((row, col, dir_row, dir_col, no_steps))

        if no_steps < 10 and (dir_row, dir_col) != (0, 0):
            nr = row + dir_row
            nc = col + dir_col
            if 0 <= nr < R and 0 <= nc < C:
                heappush(
                    queue,
                    (
                        heatloss + input[nr][nc],
                        nr,
                        nc,
                        dir_row,
                        dir_col,
                        no_steps + 1,
                    ),
                )

        if no_steps > 3 or (dir_row, dir_col) == (0, 0):
            for next_dir_row, next_dir_col in DIR.values():
                if (next_dir_row, next_dir_col) != (-dir_row, -dir_col) and (
                    next_dir_row,
                    next_dir_col,
                ) != (
                    dir_row,
                    dir_col,
                ):
                    nr = row + next_dir_row
                    nc = col + next_dir_col
                    if 0 <= nr < R and 0 <= nc < C:
                        heappush(
                            queue,
                            (
                                heatloss + input[nr][nc],
                                nr,
                                nc,
                                next_dir_row,
                                next_dir_col,
                                1,
                            ),
                        )


if __name__ == "__main__":
    input = read_input("inputs/day17.txt")
    processed_input = process_input(input)
    print(solution_1(processed_input))
