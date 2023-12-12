import math
import time


def read_input(path: str) -> tuple[str, dict[str, list[str]]]:
    with open(path, "r") as f:
        lines = f.readlines()
    instructions, nodes = lines[0].strip(), lines[2:]
    final_nodes = {}
    for node_lst in nodes:
        node = {}
        split_str = node_lst.strip().split("=")
        node[split_str[0].strip()] = split_str[1:][0].strip().split(" ")
        for _, values in node.items():
            for index, value in enumerate(values):
                values[index] = value.replace("(", "").replace(")", "").replace(",", "")
        final_nodes.update(node)

    return instructions, final_nodes


def solution(instuctions: str, nodes: dict[str, list[str]]) -> int:
    curr_node = "AAA"
    last_node = "ZZZ"
    step_count = 0
    index = 0
    while curr_node != last_node:
        if index == len(instuctions):
            index = 0

        instuction = instuctions[index]
        if instuction == "L":
            curr_node = nodes[curr_node][0]
        elif instuction == "R":
            curr_node = nodes[curr_node][1]
        index += 1

        step_count += 1

    return step_count


def solution_2(instuctions: str, nodes: dict[str, list[str]]) -> int:
    curr_nodes = [node for node in nodes.keys() if node.endswith("A")]
    all_found = [False for _ in range(len(curr_nodes))]
    first_z_encounter = [0 for _ in range(len(curr_nodes))]
    step_count = 0
    index = 0
    while not all(all_found):
        start = time.time()
        if index == len(instuctions):
            index = 0
        instuction = instuctions[index]
        if instuction == "L":
            curr_nodes = [nodes[node][0] for node in curr_nodes]
        elif instuction == "R":
            curr_nodes = [nodes[node][1] for node in curr_nodes]

        step_count += 1
        index += 1

        for i, node in enumerate(curr_nodes):
            if node.endswith("Z") and first_z_encounter[i] == 0:
                all_found[i] = True
                first_z_encounter[i] = step_count

        if step_count == 10000:
            end = time.time() - start
            return end

    return math.lcm(*first_z_encounter)


if __name__ == "__main__":
    instuctions, nodes = read_input("inputs/day8.txt")
    # print(solution(instuctions, nodes))
    print(solution_2(instuctions, nodes))
