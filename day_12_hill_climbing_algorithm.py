import math


def part_1(data):
    heightmap = []
    start = None
    goal = None
    for i, line in enumerate(data):
        heightmap.append([ord(c) - 97 for c in line.strip().replace("S", "a").replace("E", "z")])
        start = (i, line.index("S")) if "S" in line else start
        goal = (i, line.index("E")) if "E" in line else goal
    
    queue = [start]
    discovered = {start}
    steps = 0
    while queue:
        for _ in range(len(queue)):
            x, y = queue.pop(0)
            if (x, y) == goal:
                return steps
            for neighbour in neighbours(x, y):
                nx, ny = neighbour
                if (0 <= nx < len(heightmap)
                    and 0 <= ny < len(heightmap[0])
                    and neighbour not in discovered
                    and heightmap[nx][ny] - heightmap[x][y] <= 1):
                    # Can travel to the neighbour.
                    discovered.add(neighbour)
                    queue.append(neighbour)
        steps += 1
    return None


def part_2(data):
    heightmap = []
    starts = []
    goal = None
    for i, line in enumerate(data):
        heightmap.append([ord(c) - 97 for c in line.strip().replace("S", "a").replace("E", "z")])
        goal = (i, line.index("E")) if "E" in line else goal
        starts.extend((i, j) for j, c in enumerate(line) if c == "a" or c == "S")
    
    def bfs(start):
        queue = [start]
        discovered = {start}
        steps = 0
        while queue:
            for _ in range(len(queue)):
                x, y = queue.pop(0)
                if (x, y) == goal:
                    return steps
                for neighbour in neighbours(x, y):
                    nx, ny = neighbour
                    if (0 <= nx < len(heightmap)
                        and 0 <= ny < len(heightmap[0])
                        and neighbour not in discovered
                        and heightmap[nx][ny] - heightmap[x][y] <= 1):
                        # Can travel to the neighbour.
                        discovered.add(neighbour)
                        queue.append(neighbour)
            steps += 1
        return math.inf
    
    return min(bfs(start) for start in starts)


def neighbours(x, y):
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]


if __name__ == "__main__":
    with open("day_12_input.txt", "r") as f:
        inp = f.readlines()
        print("Part 1: " + str(part_1(inp)))
        print("Part 2: " + str(part_2(inp)))
