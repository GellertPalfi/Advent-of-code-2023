from typing import Literal

from common import read_input


def get_points(
    input: list[str], start: tuple[Literal[0], int], end: tuple[int, int]
) -> list[tuple[int, int]]:
    points = [start, end]
    for r, row in enumerate(input):
        for c, char in enumerate(row):
            if char == "#":
                continue
            neighbors = 0
            for nr, nc in [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]:
                if (
                    0 <= nr < len(input)
                    and 0 <= nc < len(input[0])
                    and input[nr][nc] != "#"
                ):
                    neighbors += 1
            if neighbors >= 3:
                points.append((r, c))

    return points


def get_graph(
    points: list[tuple[int, int]],
) -> dict[tuple[int, int], dict[tuple[int, int], int]]:
    graph = {pt: {} for pt in points}
    dirs = {  # noqa: F841
        "^": [(-1, 0)],
        "v": [(1, 0)],
        "<": [(0, -1)],
        ">": [(0, 1)],
        ".": [(-1, 0), (1, 0), (0, -1), (0, 1)],
    }

    for sr, sc in points:
        stack = [(0, sr, sc)]
        seen = {(sr, sc)}

        while stack:
            n, r, c = stack.pop()

            if n != 0 and (r, c) in points:
                graph[(sr, sc)][(r, c)] = n
                continue

            # for dr, dc in dirs[input[r][c]]: # part 1
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:  # part2
                nr = r + dr
                nc = c + dc
                if (
                    0 <= nr < len(input)
                    and 0 <= nc < len(input[0])
                    and input[nr][nc] != "#"
                    and (nr, nc) not in seen
                ):
                    stack.append((n + 1, nr, nc))
                    seen.add((nr, nc))

    return graph


def dfs(
    pt: tuple[int, int], graph: dict[tuple[int, int], dict[tuple[int, int], int]]
) -> int:
    if pt == end:
        return 0

    m = -float("inf")
    seen.add(pt)
    for nx in graph[pt]:
        if nx not in seen:
            m = max(m, dfs(nx, graph) + graph[pt][nx])
    seen.remove(pt)

    return m


if __name__ == "__main__":
    input = read_input("inputs/day23.txt")
    start = (0, input[0].index("."))
    end = (len(input) - 1, input[-1].index("."))
    points = get_points(input, start, end)
    graph = get_graph(points)
    seen = set()
    longest_path = dfs(start, graph)
    print(longest_path)
