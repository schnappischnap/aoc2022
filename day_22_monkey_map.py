import re


def part_1(data):
    map, instructions = data[:-2], data[-1]

    width = max(len(row) for row in map)
    map = [row.ljust(width) for row in map]
    x, y = map[0].index("."), 0
    dx, dy = 1, 0

    for steps, turn in re.findall(r"(\d+)([LR])?", instructions):
        for _ in range(int(steps)):
            new_x = x + dx
            new_y = y + dy
            try:
                new_tile = map[new_y][new_x]
                if new_tile == " ":
                    raise IndexError
            except IndexError:
                if dx == 1:
                    new_x = next((i for i, v in enumerate(map[y]) if v != " "))
                elif dx == -1:
                    new_x = next((i for i, v in reversed(list(enumerate(map[y]))) if v != " "))
                elif dy == 1:
                    new_y = next((i for i, v in enumerate(row[x] for row in map) if v != " "))
                elif dy == -1:
                    new_y = next((i for i, v in reversed(list(enumerate(row[x] for row in map))) if v != " "))

            new_tile = map[new_y][new_x]
            if new_tile == "#":
                break
            if new_tile == ".":
                x, y = new_x, new_y
        if turn == "R":
            dx, dy = -dy, dx
        elif turn == "L":
            dx, dy = dy, -dx

    facing_score = [(1, 0), (0, 1), (-1, 0), (0, -1)].index((dx, dy))
    return 1000 * (y + 1) + 4 * (x + 1) + facing_score


def part_2(data):
    map, instructions = data[:-2], data[-1]

    width = max(len(row) for row in map)
    map = [row.ljust(width) for row in map]

    map_corners = [(50, 0), (100, 0), (50, 50), (0, 100), (50, 100), (0, 150)]
    maps = [[row[x : x + 50] for row in map[y : y + 50]] for x, y in map_corners]

    map_i, x, y = 0, maps[0][0].index("."), 0
    dx, dy = 1, 0

    for steps, turn in re.findall(r"(\d+)([LR])?", instructions):
        for _ in range(int(steps)):
            new_x = x + dx
            new_y = y + dy
            new_dx = dx
            new_dy = dy
            new_map_i = map_i
            try:
                new_tile = maps[map_i][new_y][new_x]
                if new_tile == " " or new_x < 0 or new_y < 0:
                    raise IndexError
            except IndexError:
                # Hardcoded for my specific cube net.
                if dx == 1:
                    new_map_i = [1, 4, 1, 4, 1, 4][map_i]
                    new_x = [0, 49, y, 0, 49, y][map_i]
                    new_y = [y, 49 - y, 49, y, 49 - y, 49][map_i]
                    new_dx, new_dy = [(1, 0), (-1, 0), (0, -1), (1, 0), (-1, 0), (0, -1)][map_i]
                elif dx == -1:
                    new_map_i = [3, 0, 3, 0, 3, 0][map_i]
                    new_x = [0, 49, y, 0, 49, y][map_i]
                    new_y = [49 - y, y, 0, 49 - y, y, 0][map_i]
                    new_dx, new_dy = [(1, 0), (-1, 0), (0, 1), (1, 0), (-1, 0), (0, 1)][map_i]
                elif dy == 1:
                    new_map_i = [2, 2, 4, 5, 5, 1][map_i]
                    new_x = [x, 49, x, x, 49, x][map_i]
                    new_y = [0, x, 0, 0, x, 0][map_i]
                    new_dx, new_dy = [(0, 1), (-1, 0), (0, 1), (0, 1), (-1, 0), (0, 1)][map_i]
                elif dy == -1:
                    new_map_i = [5, 5, 0, 2, 2, 3][map_i]
                    new_x = [0, x, x, 0, x, x][map_i]
                    new_y = [x, 49, 49, x, 49, 49][map_i]
                    new_dx, new_dy = [(1, 0), (0, -1), (0, -1), (1, 0), (0, -1), (0, -1)][map_i]

            try:
                new_tile = maps[new_map_i][new_y][new_x]
            except IndexError:
                print(new_map_i, x, y, new_y, new_x)
                return
            if new_tile == "#":
                break
            if new_tile == ".":
                x, y = new_x, new_y
                dx, dy = new_dx, new_dy
                map_i = new_map_i
        if turn == "R":
            dx, dy = -dy, dx
        elif turn == "L":
            dx, dy = dy, -dx

    row_score = 1000 * (y + map_corners[map_i][1] + 1)
    col_score =  4 * (x + map_corners[map_i][0] + 1)
    facing_score = [(1, 0), (0, 1), (-1, 0), (0, -1)].index((dx, dy))
    return row_score + col_score + facing_score


if __name__ == "__main__":
    with open("day_22_input.txt", "r") as f:
        inp = f.read().splitlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
