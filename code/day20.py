import math
from collections import deque

from common import read_input


class Module:
    def __init__(self, name, type, destinations):
        self.name = name
        self.type = type
        self.destinations = destinations

        if type == "%":
            self.memory = "off"
        else:
            self.memory = {}


def preprocess_data(input: list[str]) -> tuple[dict[str, Module], list[str]]:
    modules = {}
    broadcast_dest = []

    for row in input:
        module, dest_modules = row.split(" -> ")
        dest_modules = dest_modules.split(", ")
        if module == "broadcaster":
            broadcast_dest = dest_modules
        else:
            module_type = module[0]
            module_name = module[1:]
            modules[module_name] = Module(module_name, module_type, dest_modules)

    for name, module in modules.items():
        for dest in module.destinations:
            if dest in modules and modules[dest].type == "&":
                modules[dest].memory[name] = "low"

    return modules, broadcast_dest


def solution1(modules: dict[str, Module], broadcast_dest) -> int:
    low = high = 0

    for _ in range(1000):
        low += 1
        q = deque([("broadcaster", x, "low") for x in broadcast_dest])

        while q:
            origin, dest, signal = q.popleft()
            if signal == "low":
                low += 1
            else:
                high += 1

            if dest not in modules:
                continue

            if modules[dest].type == "%" and signal == "low":
                next_signal = "low" if modules[dest].memory == "on" else "high"
                modules[dest].memory = "on" if modules[dest].memory == "off" else "off"
                for next_dest in modules[dest].destinations:
                    q.append((dest, next_dest, next_signal))
            elif modules[dest].type == "&":
                modules[dest].memory[origin] = signal
                if all(x == "high" for x in modules[dest].memory.values()):
                    next_signal = "low"
                else:
                    next_signal = "high"
                for next_dest in modules[dest].destinations:
                    q.append((dest, next_dest, next_signal))

    return low * high


def solution2(modules: dict[str, Module], broadcast_dest: list[str]) -> int:
    [feed] = [name for name, module in modules.items() if "rx" in module.destinations]
    cycle_lengths = {}
    seen = {
        name: False for name, module in modules.items() if feed in module.destinations
    }
    presses = 0
    while True:
        presses += 1
        q = deque([("broadcaster", x, "low") for x in broadcast_dest])

        while q:
            origin, dest, signal = q.popleft()
            if dest not in modules:
                continue

            if modules[dest].name == feed and signal == "high":
                seen[origin] = True

                if origin not in cycle_lengths:
                    cycle_lengths[origin] = presses
                if all(seen.values()):
                    return math.lcm(*cycle_lengths.values())

            if modules[dest].type == "%" and signal == "low":
                next_signal = "low" if modules[dest].memory == "on" else "high"
                modules[dest].memory = "on" if modules[dest].memory == "off" else "off"
                for next_dest in modules[dest].destinations:
                    q.append((dest, next_dest, next_signal))
            elif modules[dest].type == "&":
                modules[dest].memory[origin] = signal
                if all(x == "high" for x in modules[dest].memory.values()):
                    next_signal = "low"
                else:
                    next_signal = "high"
                for next_dest in modules[dest].destinations:
                    q.append((dest, next_dest, next_signal))


if __name__ == "__main__":
    data = read_input("inputs/day20.txt")
    modules, broadcast_dest = preprocess_data(data)
    # print(solution1(modules, broadcast_dest))
    print(solution2(modules, broadcast_dest))
