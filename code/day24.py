import sympy


def solution_1(hailstones: list[tuple[int]]) -> int:
    total = 0
    for i, hs1 in enumerate(hailstones):
        for hs2 in hailstones[:i]:
            px, py = sympy.symbols("px py")
            answers = sympy.solve(
                [
                    vy * (px - sx) - vx * (py - sy)
                    for sx, sy, _, vx, vy, _ in [hs1, hs2]
                ],
            )
            if answers == []:
                continue
            x, y = answers[px], answers[py]
            if (
                200000000000000 <= x <= 400000000000000
                and 200000000000000 <= y <= 400000000000000
            ):
                if all(
                    (x - sx) * vx >= 0 and (y - sy) * vy >= 0
                    for sx, sy, _, vx, vy, _ in [hs1, hs2]
                ):
                    total += 1
    return total


def solution_2(hailstones: list[tuple[int]]) -> int:
    xr, yr, zr, vxr, vyr, vzr = sympy.symbols("xr yr zr vxr vyr vzr")
    equations = []
    for i, (sx, sy, sz, vx, vy, vz) in enumeratecpo(hailstones):
        equations.append((xr - sx) * (vy - vyr) - (yr - sy) * (vx - vxr))
        equations.append((yr - sy) * (vz - vzr) - (zr - sz) * (vy - vyr))
        # x % 1 == 0 checks if x is an integer
        # because we need an int solution
        answers = [
            sol
            for sol in sympy.solve(equations)
            if all(x % 1 == 0 for x in sol.values())
        ]
        if i < 2:
            continue
        if len(answers) == 1:
            break

    return answers[0][xr] + answers[0][yr] + answers[0][zr]


if __name__ == "__main__":
    hailstones = [
        tuple(map(int, line.replace("@", ",").split(",")))
        for line in open("inputs/day24.txt")
    ]
    # print(solution_1(hailstones))
    print(solution_2(hailstones))
