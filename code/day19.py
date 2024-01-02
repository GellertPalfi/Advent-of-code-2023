def read_input(
    path: str,
) -> tuple[
    dict[str, tuple[list[tuple[str, str, int, str]], str]], list[dict[str, int]]
]:
    parts = []
    workflows = {}
    with open(path, "r") as f:
        split_workflows, split_parts = f.read().split("\n\n")
        split_parts = split_parts.split("\n")
        for part in split_parts:
            final_part = (
                part.replace("=", ":")
                .replace("x", '"x"')
                .replace("m", '"m"')
                .replace("a", '"a"')
                .replace("s", '"s"')
            )
            parts.append(eval(final_part))

        split_workflows = split_workflows.split("\n")
        for workflow in split_workflows:
            name, rules = workflow[:-1].split("{")
            rules = rules.split(",")
            workflows[name] = ([], rules.pop())
            for rule in rules:
                comparison, next_step = rule.split(":")
                key = comparison[0]
                operator = comparison[1]
                num = int(comparison[2:])
                workflows[name][0].append((key, operator, num, next_step))

    return workflows, parts


def accepted(
    part: list[dict[str, int]],
    workflows: dict[str, tuple[list[tuple[str, str, int, str]], str]],
    workflow: str = "in",
) -> bool:
    if workflow == "A":
        return 1
    if workflow == "R":
        return 0

    rule = workflows[workflow][0]
    fallback_rule = workflows[workflow][1]
    for key, operator, num, next_step in rule:
        if operator == "<":
            if part[key] < num:
                return accepted(part, workflows, next_step)
        elif operator == ">":
            if part[key] > num:
                return accepted(part, workflows, next_step)
    else:
        return accepted(part, workflows, fallback_rule)


def solution_1(
    workflows: dict[str, tuple[list[tuple[str, str, int, str]], str]],
    parts: list[dict[str, int]],
) -> int:
    total_sum = 0
    for part in parts:
        if accepted(part, workflows):
            total_sum += sum(part.values())
    return total_sum


def count_range(
    ranges: dict[str, tuple[int, int]],
    workflows: dict[str, tuple[list[tuple[str, str, int, str]], str]],
    workflow: str = "in",
) -> int:
    if workflow == "R":
        return 0
    if workflow == "A":
        product = 1
        for lower, upper in ranges.values():
            product *= upper - lower + 1
        return product

    total_sum = 0

    rules, fallback = workflows[workflow]
    for key, operator, num, next_step in rules:
        low, high = ranges[key]
        # calculte range endpoints
        if operator == "<":
            accepted_parts = (low, num - 1)
            rejected_parts = (num, high)
        if operator == ">":
            accepted_parts = (num + 1, high)
            rejected_parts = (low, num)
        # check if range is empy
        if accepted_parts[0] < accepted_parts[1]:
            copy = dict(ranges)
            copy[key] = accepted_parts
            total_sum += count_range(copy, workflows, next_step)
        if rejected_parts[0] < rejected_parts[1]:
            ranges = dict(ranges)
            ranges[key] = rejected_parts

    total_sum += count_range(ranges, workflows, fallback)

    return total_sum


def solution_2(
    workflows: dict[str, tuple[list[tuple[str, str, int, str]], str]],
) -> int:
    return count_range({key: (1, 4000) for key in "xmas"}, workflows)


if __name__ == "__main__":
    workflows, parts = read_input("inputs/day19_sample.txt")
    print(solution_1(workflows, parts))
    print(solution_2(workflows))
