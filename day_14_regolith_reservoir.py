import itertools


def part_1(data):
    rocks = set()
    for line in data:
        lines = [tuple(int(i) for i in coord.split(",")) for coord in line.split("->")]
        for start, end in zip(lines, lines[1:]):
            rocks.update(
                (x, y) 
                for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1) 
                for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1)
            )

    abyss_y = max(rock[1] for rock in rocks)
    for i in itertools.count():
        x, y = 500, 0
        settled = False
        while not settled:
            if y >= abyss_y:
                return i
            for pos in [(x, y+1), (x-1, y+1), (x+1, y+1)]:
                if pos not in rocks:
                    x, y = pos
                    break
            else:
                rocks.add((x, y))
                settled = True


def part_2(data):
    rocks = set()
    for line in data:
        lines = [tuple(int(i) for i in coord.split(",")) for coord in line.split("->")]
        for start, end in zip(lines, lines[1:]):
            rocks.update(
                (x, y) 
                for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1) 
                for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1)
            )

    floor_y = max(rock[1] for rock in rocks) + 2
    for i in itertools.count():
        x, y = (500, 0)
        settled = False
        while not settled:
            for pos in [(x, y+1), (x-1, y+1), (x+1, y+1)]:
                if pos not in rocks and pos[1] != floor_y:
                    x, y = pos
                    break
            else:
                rocks.add((x, y))
                settled = True
        if (x, y) == (500, 0):
            return i + 1


if __name__ == "__main__":
    with open("day_14_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
