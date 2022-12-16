from collections import defaultdict
import functools
import itertools
import math
import re


def part_1(data):
    valves = []
    flow_rates = dict()
    distances = defaultdict(lambda: math.inf)
    for line in data:
        valve, flow, neighbours = re.search(r"([A-Z]{2}).*=(\d+).*valves? (.*)", line).groups()
        valves.append(valve)
        if flow != "0":
            flow_rates[valve] = int(flow)
        for neighbour in neighbours.split(", "):
            distances[neighbour, valve] = 1

    # Floyd–Warshall algorithm to find the shortest paths.
    for k, i, j in itertools.product(valves, repeat=3):
        distances[i, j] = min(distances[i, j], distances[i, k] + distances[k, j])

    @functools.cache
    def search(valve, time=30, closed=frozenset(flow_rates)):
        most_pressure_released = 0
        for other_valve in closed:
            distance = distances[valve, other_valve]
            if distance < time:
                new_time = time - distance - 1
                pressure = (flow_rates[other_valve] * new_time
                            + search(other_valve, new_time, closed - {other_valve}))
                most_pressure_released = max(most_pressure_released, pressure)
        return most_pressure_released

    return search("AA")


def part_2(data):
    valves = []
    flow_rates = dict()
    distances = defaultdict(lambda: math.inf)
    for line in data:
        valve, flow, neighbours = re.search(r"([A-Z]{2}).*=(\d+).*valves? (.*)", line).groups()
        valves.append(valve)
        if flow != "0":
            flow_rates[valve] = int(flow)
        for neighbour in neighbours.split(", "):
            distances[neighbour, valve] = 1

    for k, i, j in itertools.product(valves, repeat=3):
        distances[i, j] = min(distances[i, j], distances[i, k] + distances[k, j])

    @functools.cache
    def search(valve, time=26, closed=frozenset(flow_rates), elephant=False):
        most_pressure_released = 0
        for other_valve in closed:
            distance = distances[valve, other_valve]
            if distance < time:
                new_time = time - distance - 1
                pressure = (flow_rates[other_valve] * new_time
                            + search(other_valve, new_time, closed - {other_valve}, elephant))
                most_pressure_released = max(most_pressure_released, pressure)
        if elephant:
            most_pressure_released = max(most_pressure_released, search("AA", closed=closed))
        return most_pressure_released

    return search("AA", elephant=True)


if __name__ == "__main__":
    with open("day_16_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
