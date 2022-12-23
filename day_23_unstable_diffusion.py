from collections import Counter
import itertools


def part_1(data):
    elves = {(x, y) for y, row in enumerate(data) for x, c in enumerate(row) if c == "#"}
    moves = [
        [(0, -1), (-1, -1), (1, -1)],
        [(0, 1), (-1, 1), (1, 1)],
        [(-1, 0), (-1, -1), (-1, 1)],
        [(1, 0), (1, -1), (1, 1)],
    ]
    for _ in range(10):
        propositions = []
        positions_counter = Counter()

        for (x, y) in elves:
            if not any((nx, ny) in elves for nx, ny in neighbours(x, y)):
                propositions.append(((x, y), (x, y)))
            else:
                for move in moves:
                    if not any((x + dx, y + dy) in elves for dx, dy in move):
                        new_position = (x + move[0][0], y + move[0][1])
                        propositions.append((new_position, (x, y)))
                        positions_counter[new_position] += 1
                        break
                else:
                    propositions.append(((x, y), (x, y)))

        new_elves = set()
        for new_position, old_position in propositions:
            new_elves.add(new_position if positions_counter[new_position] == 1 else old_position)
        elves = new_elves
        moves = moves[1:] + moves[:1]

    min_x = min(x for x, _ in elves)
    min_y = min(y for _, y in elves)
    max_x = max(x for x, _ in elves)
    max_y = max(y for _, y in elves)
    return (max_y - min_y + 1) * (max_x - min_x + 1) - len(elves)


def part_2(data):
    elves = {(x, y) for y, row in enumerate(data) for x, c in enumerate(row) if c == "#"}
    moves = [
        [(0, -1), (-1, -1), (1, -1)],
        [(0, 1), (-1, 1), (1, 1)],
        [(-1, 0), (-1, -1), (-1, 1)],
        [(1, 0), (1, -1), (1, 1)],
    ]
    for i in itertools.count(1):
        propositions = []
        positions_counter = Counter()

        for (x, y) in elves:
            if not any((nx, ny) in elves for nx, ny in neighbours(x, y)):
                propositions.append(((x, y), (x, y)))
            else:
                for move in moves:
                    if not any((x + dx, y + dy) in elves for dx, dy in move):
                        new_position = (x + move[0][0], y + move[0][1])
                        propositions.append((new_position, (x, y)))
                        positions_counter[new_position] += 1
                        break
                else:
                    propositions.append(((x, y), (x, y)))

        new_elves = set()
        for new_position, old_position in propositions:
            new_elves.add(new_position if positions_counter[new_position] == 1 else old_position)
        if elves == new_elves:
            return i
        elves = new_elves
        moves = moves[1:] + moves[:1]


def neighbours(x, y):
    return [(x + dx, y + dy) for dx in range(-1, 2) for dy in range(-1, 2) if dx != 0 or dy != 0]


if __name__ == "__main__":
    with open("day_23_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
