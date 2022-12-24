def part_1(data):
    directions = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
    blizzards = [
        ((x - 1, y - 1), directions[c])
        for y, row in enumerate(data)
        for x, c in enumerate(row)
        if c in directions
    ]
    width = len(data[0].strip()) - 2
    height = len(data) - 2

    def bfs(start, goal):
        queue = [(start, 0)]
        discovered = {(start, 0)}
        discovered_blizzards = dict()
        while queue:
            (x, y), steps = queue.pop(0)
            if (x, y) == goal:
                return steps

            if (steps + 1) not in discovered_blizzards:
                discovered_blizzards[steps + 1] = get_blizzards(steps + 1)
            blizzard_positions = discovered_blizzards[steps + 1]

            for nx, ny in neighbours(x, y):
                if (
                    ((0 <= nx < width and 0 <= ny < height) or ((nx, ny) in [start, goal]))
                    and (nx, ny) not in blizzard_positions
                    and ((nx, ny), steps + 1) not in discovered):
                    discovered.add(((nx, ny), steps + 1))
                    queue.append(((nx, ny), steps + 1))

    def get_blizzards(minute):
        return set(
            ((x + dx * minute) % width, (y + dy * minute) % height)
            for (x, y), (dx, dy) in blizzards
        )

    return bfs((0, -1), (width - 1, height))


def part_2(data):
    directions = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
    blizzards = [
        ((x - 1, y - 1), directions[c])
        for y, row in enumerate(data)
        for x, c in enumerate(row)
        if c in directions
    ]
    width = len(data[0].strip()) - 2
    height = len(data) - 2

    def bfs(start, goal, time_start=0):
        queue = [(start, time_start)]
        discovered = {(start, time_start)}
        discovered_blizzards = dict()
        while queue:
            (x, y), steps = queue.pop(0)
            if (x, y) == goal:
                return steps

            if (steps + 1) not in discovered_blizzards:
                discovered_blizzards[steps + 1] = get_blizzards(steps + 1)
            blizzard_positions = discovered_blizzards[steps + 1]

            for nx, ny in neighbours(x, y):
                if (
                    ((0 <= nx < width and 0 <= ny < height) or ((nx, ny) in [start, goal]))
                    and (nx, ny) not in blizzard_positions
                    and ((nx, ny), steps + 1) not in discovered):
                    discovered.add(((nx, ny), steps + 1))
                    queue.append(((nx, ny), steps + 1))

    def get_blizzards(minute):
        return set(
            ((x + dx * minute) % width, (y + dy * minute) % height)
            for (x, y), (dx, dy) in blizzards
        )

    start = (0, -1)
    goal = (width - 1, height)
    return bfs(start, goal, bfs(goal, start, bfs((0, -1), (width - 1, height))))


def neighbours(x, y):
    return [(x + dx, y + dy) for dx, dy in [(0, -1), (0, 1), (-1, 0), (1, 0), (0, 0)]]


if __name__ == "__main__":
    with open("day_24_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
