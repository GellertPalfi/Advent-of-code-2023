import networkx as nx
from common import read_input


def solution_1(input: list[str]) -> int:
    for line in input:
        left, right = line.split(":")
        for node in right.strip().split():
            graph.add_edge(left, node)
            graph.add_edge(node, left)

    graph.remove_edges_from(nx.minimum_edge_cut(graph))
    a, b = nx.connected_components(graph)

    return len(a) * len(b)


if __name__ == "__main__":
    graph = nx.Graph()
    input = read_input("inputs/day25.txt")
    print(solution_1(input))
