from collections import deque

from common import read_input


def preprocess_input(input: list[str]) -> list[list[int]]:
    return [list(map(int, line.replace("~", ",").split(","))) for line in input]


def overlaps(brick1: list[int], brick2: list[int]) -> bool:
    return max(brick1[0], brick2[0]) <= min(brick1[3], brick2[3]) and max(
        brick1[1], brick2[1]
    ) <= min(brick1[4], brick2[4])


def drop_bricks(bricks: list[list[int]]) -> list[list[int]]:
    bricks.sort(key=lambda brick: brick[2])
    for i, brick in enumerate(bricks):
        max_height = 1
        for next_brick in bricks[:i]:
            if overlaps(brick, next_brick):
                max_height = max(max_height, next_brick[5] + 1)
            brick[5] -= brick[2] - max_height
            brick[2] = max_height

    return bricks


def solution_1(bricks: list[list[int]]) -> int:
    total_sum = 0
    k_supports_v = {i: set() for i in range(len(bricks))}
    v_supports_k = {i: set() for i in range(len(bricks))}

    for j, upper in enumerate(bricks):
        for i, lower in enumerate(bricks[:j]):
            if overlaps(lower, upper) and upper[2] == lower[5] + 1:
                k_supports_v[i].add(j)
                v_supports_k[j].add(i)

    for i in range(len(bricks)):
        if all([len(v_supports_k[j]) >= 2 for j in k_supports_v[i]]):
            total_sum += 1

    return total_sum, k_supports_v, v_supports_k


def solution_2(
    bricks: list[list[int]], k_supports_v: dict[str, set], v_supports_k: dict[str, set]
) -> int:
    total = 0
    for i in range(len(bricks)):
        q = deque(j for j in k_supports_v[i] if len(v_supports_k[j]) == 1)
        falling = set(q)
        falling.add(i)

        while q:
            j = q.popleft()
            for k in k_supports_v[j] - falling:
                if v_supports_k[k] <= falling:
                    q.append(k)
                    falling.add(k)

        total += len(falling) - 1

    return total


if __name__ == "__main__":
    input = read_input("inputs/day22.txt")
    processed_input = preprocess_input(input)
    bricks = drop_bricks(processed_input)
    total, k_supports_v, v_supports_k = solution_1(bricks)
    print(solution_2(bricks, k_supports_v, v_supports_k))
