import re


def part_1(data):
    elves = [[int(i) for i in re.findall(r"(\d+)", line)] for line in data]
    return sum(
        (e0 <= e2 and e1 >= e3) or (e0 >= e2 and e1 <= e3)
        for e0, e1, e2, e3 in elves
    )


def part_2(data):
    elves = [[int(i) for i in re.findall(r"(\d+)", line)] for line in data]
    return sum(e0 <= e3 and e1 >= e2 for e0, e1, e2, e3 in elves)


if __name__ == "__main__":
    with open("day_04_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
